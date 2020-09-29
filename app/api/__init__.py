import asyncio
from flask_restful import Api
from app import config
from .auth import Register, Login, Logout
from .task import TaskStatusAPI, DataProcessingAPI

api_restful = Api(prefix=config.settings.BaseConfig.API_PREFIX)
        
# data processing endpoint
api_restful.add_resource(DataProcessingAPI, '/queue/process_data')

# task status endpoint
api_restful.add_resource(TaskStatusAPI, '/queue/tasks/<string:task_id>')

# Auth endpoint
api_restful.add_resource(Register, '/user/register')
api_restful.add_resource(Login, '/user/login')
api_restful.add_resource(Logout, '/user/logout')
