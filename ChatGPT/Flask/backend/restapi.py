from flask import Flask, request
from flask_restx import Api, Resource, fields
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # 이 부분이 CORS를 적용하는 부분입니다.
api = Api(app)

tasks = []

task = api.model('Task', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})

class TaskList(Resource):
    @api.doc('list_tasks')
    @api.marshal_list_with(task)
    def get(self):
        '''List all tasks'''
        return tasks

    @api.doc('create_task')
    @api.expect(task)
    @api.marshal_with(task, code=201)
    def post(self):
        '''Create a new task'''
        new_task = api.payload
        new_task['id'] = len(tasks) + 1
        tasks.append(new_task)
        return new_task, 201

class Task(Resource):
    @api.doc('get_task')
    @api.marshal_with(task)
    def get(self, task_id):
        '''Fetch a task given its identifier'''
        for task in tasks:
            if task['id'] == task_id:
                return task
        api.abort(404)

    @api.doc('update_task')
    @api.expect(task)
    @api.marshal_with(task)
    def put(self, task_id):
        '''Update a task given its identifier'''
        for task in tasks:
            if task['id'] == task_id:
                task.update(api.payload)
                return task
        api.abort(404)

    @api.doc('delete_task')
    @api.response(204, 'Task deleted')
    def delete(self, task_id):
        '''Delete a task given its identifier'''
        global tasks
        tasks = [task for task in tasks if task['id'] != task_id]
        return '', 204

api.add_resource(TaskList, '/tasks')
api.add_resource(Task, '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(debug=True)