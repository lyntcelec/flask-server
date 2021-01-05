from celery import Celery
from .. import config
import time
from multiprocessing import Process, Queue

CeleryQueueMessages = Queue()


class MonitorThread(object):
    def __init__(self, celery_app, celery_queue, interval=2):
        self.celery_app = celery_app
        self.celery_queue = celery_queue
        self.interval = interval

        self.state = self.celery_app.events.State()

        self.thread = Process(name="MonitorThread", target=self.run, args=())
        self.thread.daemon = True
        self.thread.start()

    def catchall(self, event):
        if event["type"] != "worker-heartbeat":
            self.celery_queue.put(event)

    def run(self):
        while True:
            try:
                with self.celery_app.connection() as connection:
                    recv = self.celery_app.events.Receiver(
                        connection, handlers={"*": self.catchall}
                    )
                    recv.capture(limit=None, timeout=None, wakeup=True)

            except (KeyboardInterrupt, SystemExit):
                raise

            except Exception:
                # unable to capture
                pass

            time.sleep(self.interval)


def make_celery():
    env = config.settings.BaseConfig

    celery = Celery(
        __name__, broker=env.CELERY_BROKER, backend=env.CELERY_RESULT_BACKEND
    )

    MonitorThread(celery, CeleryQueueMessages)
    return celery


celery = make_celery()


@celery.task()
def process_data(i):
    time.sleep(5)
    return i * 2
