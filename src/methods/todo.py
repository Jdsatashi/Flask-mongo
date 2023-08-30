from _datetime import datetime

from bson import ObjectId
from flask import render_template, request, flash, redirect

from src import app, todo_table
from ..forms import TodoForm


@app.route('/todos/')
def todo_index():
    list_todos = list(todo_table.find().sort('date_created', -1))
    todos = []
    for todo in list_todos:
        todo["_id"] = str(todo["_id"])
        todo["date_created"] = todo["date_created"].strftime("%b %d %Y | %H:%M:%S")
        todos.append(todo)
    # return todos
    return render_template('todo/index.html', todos=todos, title="Todos list")


@app.route('/todo/add', methods=['GET', 'POST'])
def todo_create():
    if request.method == "POST":
        form = TodoForm(request.form)

        todo_table.insert_one({
            "name": form.name.data,
            "description": form.description.data,
            "completed": form.completed.data,
            "date_created": datetime.utcnow()
        })
        flash("Todo successfully added", "success")
        return redirect("/todos/")
    else:
        form = TodoForm()
    return render_template("todo/create.html", form=form)


@app.route('/todo/details/<string:todo_id>', methods=['GET', 'POST', 'DELETE'])
def todo_details(todo_id):
    form = TodoForm(request.form)
    if request.method == 'GET':
        todo_detail = todo_table.find_one({
            '_id': ObjectId(todo_id)
        })
        if todo_detail:
            todo_detail["_id"] = str(todo_detail["_id"])
            todo_detail["date_created"] = todo_detail["date_created"].strftime("%b %d %Y | %H:%M:%S")
            todo_data = [todo_detail]
            return render_template('todo/show.html', todos=todo_data, form=form)
        else:
            return "404: This todo is not exist!"

    if request.method == 'POST':
        todo_table.find_one_and_update({
            '_id': ObjectId(todo_id)}, {
            "$set": {
                "name": form.name.data,
                "description": form.description.data,
                "completed": form.completed.data,
                "date_created": datetime.utcnow()
            }
        })
        flash("Todo successfully updated", "success")
        return redirect("/todo/details/" + todo_id)


@app.route('/todo/delete/<todo_id>')
def todo_delete(todo_id):
    todo_table.find_one_and_delete({'_id': ObjectId(todo_id)})
    flash("Todo successfully deleted", "success")
    return redirect("/todos/")
