from bson import ObjectId
from flask import render_template, request, flash, redirect

from src import app, todo_table
from .forms import TodoForm
from .methods.todo import todo_get_index, todo_get_create, todo_get_show, todo_get_update


@app.route('/todos/')
def todo_index():
    todos = todo_get_index()
    return render_template(
        'todo/index.html',
        todos=todos,
        title="Todos list")


@app.route('/todo/add', methods=['GET', 'POST'])
def todo_create():
    if request.method == "POST":
        todo_get_create()
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
            todo_data = todo_get_show(todo_detail)
            return render_template('todo/show.html', todos=todo_data, form=form)
        else:
            return "404: This todo is not exist!"

    if request.method == 'POST':
        todo_get_update(todo_id, form)
        flash("Todo successfully updated", "success")
        return redirect("/todo/details/" + todo_id)


@app.route('/todo/delete/<todo_id>')
def todo_delete(todo_id):
    todo_table.find_one_and_delete({'_id': ObjectId(todo_id)})
    flash("Todo successfully deleted", "success")
    return redirect("/todos/")
