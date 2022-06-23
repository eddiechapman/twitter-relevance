from flask_wtf import FlaskForm
from wtforms import FileField, RadioField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ArticleForm(FlaskForm):
    relevance = RadioField(label="Relevance", choices=[("yes", "Yes"), ("no", "No"), ("unsure", "Unsure")], validators=[DataRequired()])
    comments = TextAreaField(label="Comments")
    submit = SubmitField(label="Submit")


class ImportForm(FlaskForm):
    file = FileField()
