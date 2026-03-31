from app.forms.base import ModelForm

from .fields import document_field, name_field, phone_field


class StudentForm(ModelForm):
    document_id = document_field()
    name = name_field()
    phone = phone_field()
