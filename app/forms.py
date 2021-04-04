from flask_wtf import FlaskForm
from flask import Flask
from werkzeug.utils import secure_filename
from flask_wtf.file import FileRequired, FileField, FileAllowed
from wtforms.validators import InputRequired
from wtforms import StringField

class UploadForm(FlaskForm):
    description = StringField('Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
