import time
from app.tasks import celery, process_data
from flask_restful import Resource
from flask import jsonify

class TaskStatusAPI(Resource):
    def get(self, task_id):
        print("task_id", task_id)
        task = celery.AsyncResult(task_id)
        return jsonify(task.result)

class DataProcessingAPI(Resource):
    def get(self):
        task = process_data.delay(2)
        return {'task_id': task.id}, 200
