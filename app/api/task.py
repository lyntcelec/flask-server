import time
from app.tasks import celery, process_data
from flask_restful import Resource
from flask import jsonify
from multiprocessing import Process

class TaskStatusAPI(Resource):
    def get(self, task_id):
        print("task_id", task_id)
        task = celery.AsyncResult(task_id)
        return jsonify(task.result)

class DataProcessingAPI(Resource):
    def get(self):
        task = process_data.delay(2)
        return {'task_id': task.id}, 200

class CeleryProcessing(object):
    def __init__(self, celery_queue):
        self.celery_queue = celery_queue
        self.thread = Process(name="CeleryProcessing", target=self.run, args=(self.celery_queue,))
        self.thread.daemon = True
        self.thread.start()

    def run(self, celery_queue):
        while True:
            celery_event = celery_queue.get()
            if (celery_event["type"] == "task-succeeded"):
                task = celery.AsyncResult(celery_event["uuid"])
                print(task.result)