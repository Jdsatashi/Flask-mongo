from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    name = StringField("Name", [DataRequired()])
    description = StringField("Description", [DataRequired()])
    completed = SelectField("Completed", [DataRequired()], choices=[("False", "False"), ("True", "True")])
    submit = SubmitField("Add todo")
