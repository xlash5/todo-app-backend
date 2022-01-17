from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt,
    jwt_required,
    current_user
)
from models.user import UserModel
from models.task import TaskModel

_add_task_parser = reqparse.RequestParser()
_add_task_parser.add_argument('task_text',
                              type=str,
                              required=True,
                              help="This field cannot be blank."
                              )

_delete_task_parser = reqparse.RequestParser()
_delete_task_parser.add_argument('task_id',
                                 type=str,
                                 required=True,
                                 help="This field cannot be blank."
                                 )

_edit_task_parser = reqparse.RequestParser()
_edit_task_parser.add_argument('task_text',
                               type=str,
                               required=True,
                               help="This field cannot be blank."
                               )
_edit_task_parser.add_argument('task_id',
                               type=str,
                               required=True,
                               help="This field cannot be blank."
                               )


class Task(Resource):
    @jwt_required()
    def post(self):
        data = _add_task_parser.parse_args()
        user = current_user

        task = TaskModel(
            task_text=data['task_text'], owner_id=user.json()['id'])
        task.save_to_db()

        return {"task_text": data['task_text'], "success": "Task created successfully"}, 201

    @jwt_required()
    def get(self):
        user = current_user
        tasks = TaskModel.find_by_owner_id(user.json()['id'])

        return {"tasks": [task.json() for task in tasks]}, 200

    # @jwt_required()
    # def delete(self):
    #     data = _delete_task_parser.parse_args()
    #     user = current_user
    #     task = TaskModel.find_by_task_id(data['task_id'])

    #     if user.json()['id'] != task.owner_id:
    #         return {"error": "You are not allowed to delete this task"}, 401

    #     task.delete_from_db()

    #     return {"msg": "Task deleted successfully"}, 201

    @jwt_required()
    def put(self):
        data = _edit_task_parser.parse_args()
        user = current_user
        task = TaskModel.find_by_task_id(data['task_id'])

        if user.json()['id'] != task.owner_id:
            return {"error": "You are not allowed to delete this task"}, 401

        if task:
            task.task_text = data['task_text']
        else:
            return {"msg": "Task not found"}, 404

        task.save_to_db()

        return task.json(), 200


class DeleteTask(Resource):
    @jwt_required()
    def post(self):
        data = _delete_task_parser.parse_args()
        user = current_user
        task = TaskModel.find_by_task_id(data['task_id'])

        if user.json()['id'] != task.owner_id:
            return {"error": "You are not allowed to delete this task"}, 401

        task.delete_from_db()

        return {"msg": "Task deleted successfully"}, 201
