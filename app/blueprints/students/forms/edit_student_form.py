from flask_wtf import FlaskForm
from wtforms import SubmitField

from .fields import document_field, name_field, phone_field


class EditStudentForm(FlaskForm):
    document_id = document_field()
    name = name_field()
    phone = phone_field()

    submit = SubmitField("Actualizar")
