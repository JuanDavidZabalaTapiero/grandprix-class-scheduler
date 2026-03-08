from app.forms.base import ModelForm
from app.forms.common_fields import name_field, phone_field

from .fields import document_field


class EditStudentForm(ModelForm):
    document_id = document_field()
    name = name_field()
    phone = phone_field()
