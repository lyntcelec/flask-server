from celery import Celery
from .. import config
import time
import threading

class MonitorThread(object):
    def __init__(self, celery_app, interval=2):
        self.celery_app = celery_app
        self.interval = interval

        self.state = self.celery_app.events.State()

        self.thread = threading.Thread(target=self.run, args=())
        self.thread.daemon = True
        self.thread.start()

    def catchall(self, event):
        if event['type'] != 'worker-heartbeat':
            # logic here
            print ("[event]", event)

    def run(self):
        while True:
            try:
                with self.celery_app.connection() as connection:
                    recv = self.celery_app.events.Receiver(connection, handlers={
                        '*': self.catchall
                    })
                    recv.capture(limit=None, timeout=None, wakeup=True)

            except (KeyboardInterrupt, SystemExit):
                raise

            except Exception:
                # unable to capture
                pass

            time.sleep(self.interval)

def make_celery():
    if config.settings.BaseConfig.ENV == "production":
        env = config.settings.ProductionConfig
    else:
        env = config.settings.DevelopmentConfig

    celery = Celery(__name__, broker=env.CELERY_BROKER, backend=env.CELERY_RESULT_BACKEND)
    celery.conf.update(CELERY_SEND_EVENTS=True)
    return celery

celery = make_celery()

@celery.task()
def process_data(i):
    time.sleep(5)
    return i*2