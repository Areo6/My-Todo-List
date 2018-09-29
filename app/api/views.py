from flask import Blueprint, jsonify, request
from api.models import User, Tasks


mod = Blueprint('api', __name__)
user = User()
task = Tasks()

@mod.route("/api/register", methods= ["POST"])
def register():
    """
    This route Registers a new user
    """
    data = request.json
    if not data:
        return jsonify({"Message": "Bad request. Your input should be a dictionary"}), 400
    if not 'name' in data or not 'email' in data or not 'password' in data:
        return jsonify({"Message": "Bad format. Please specify user Name, Email and Password"}), 400
    if len(data) > 3:
        return jsonify({"Message": "Too many arguments. Only Name, Email and Password are required"}), 414
    register = user.add_account(data["name"], data["email"], data['password'])
    if register != "Successfully Added an account":
        return jsonify({"Message": register}), 417
    return jsonify({"Message": register}), 201

@mod.route("/api/login", methods = ["POST"])
def login():
    """
    This endpoint Logs the user in 
    """
    data = request.json
    if not data:
        return jsonify({"Message": "Bad request. Your input should be a dictionary"}), 400
    if not "email" in data or not "password" in data:
        return jsonify({"Message": "Bad format. Please specify user Email and Password"}), 400
    if len(data) > 2:
        return jsonify({"Message": "Too many arguments. Only Email and Password are required"}), 414
    login = user.login(data['email'], data['password'])
    if login != "You have successfully logged in":
        return jsonify({"Message": login}), 403
    return jsonify({"Message": login}), 200

@mod.route("/api/tasks", methods = ["GET"])
def get_tasks():
    """
    This endpoint is used to View alls the tasks
    """
    item = task.view_tasks()
    return jsonify({"Message": item}), 200

@mod.route("/api/tasks", methods = ["POST"])
def post_task():
    """
    This endpoint servers to post a new task
    """
    data = request.json
    if not data:
        return jsonify({"Message": "Bad request. Your input should be a dictionary"}), 400
    if not "task" in data:
        return jsonify({"Message": "Bad format. Please specify Task"}), 400
    if len(data) > 1:
        return jsonify({"Message": "Too many arguments. Only Task is required"}), 414
    item = task.create_task(data["task"])
    if item != "Successfully Created Todo task":
        return jsonify({"Message": item}), 417
    return jsonify({"Message": item}), 201

@mod.route("/api/tasks/<int:task_id>", methods = ["DELETE"])
def delete_task(task_id):
    """
    This endpoint is used to delete a task from the datastructure
    """
    item = task.delete_task(task_id)
    if item == "{} does not exist in the todo list. Please enter an existing id".format(task_id):
        return jsonify({"Message": item}), 404
    if item != "Task Number {} successfuly deleted".format(task_id):
        return jsonify({"Message": item}), 417
    return jsonify({"Message": item}), 202

@mod.route("/api/tasks/<int:task_id>", methods = ["PUT"])
def Mark_task_as_finished(task_id):
    """
    This endpoint updates a task by marking it as finished
    """
    item = task.mark_as_finished(task_id)
    if item == "{} does not exist in the todo list. Please enter an existing id".format(task_id):
        return jsonify({"Message": item}), 404
    if item != "Successfully Marked task {} as Finished".format(task_id):
        return jsonify({"Message": item}), 417
    return jsonify({"Message": item}), 200

@mod.route("/api/tasks", methods = ["DELETE"])
def delete_all_tasks():
    """
    This endpoint deletes all the tasks from the the datastructure
    """
    item = task.delete_all_tasks()
    if item != "Successfully emptied Todo list":
        return jsonify({"Message": item}), 404
    return jsonify({"Message": item}), 202
    