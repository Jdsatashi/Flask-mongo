from bson import ObjectId
from src import todo_table
from src.forms import TodoForm
from flask import request
from _datetime import datetime


def todo_get_index():
    list_todos = list(todo_table.find().sort('date_created', -1))
    todos = []
    for todo in list_todos:
        todo["_id"] = str(todo["_id"])
        todo["date_created"] = todo["date_created"].strftime("%b %d %Y | %H:%M:%S")
        todos.append(todo)
    return todos


def todo_get_create():
    form = TodoForm(request.form)
    todo_table.insert_one({
        "name": form.name.data,
        "description": form.description.data,
        "completed": form.completed.data,
        "date_created": datetime.utcnow()
    })


def todo_get_show(todo_detail):
    todo_detail["_id"] = str(todo_detail["_id"])
    todo_detail["date_created"] = todo_detail["date_created"].strftime("%b %d %Y | %H:%M:%S")
    return [todo_detail]


def todo_get_update(todo_id, form):
    todo_table.find_one_and_update({
        '_id': ObjectId(todo_id)}, {
        "$set": {
            "name": form.name.data,
            "description": form.description.data,
            "completed": form.completed.data,
            "date_created": datetime.utcnow()
        }
    })
