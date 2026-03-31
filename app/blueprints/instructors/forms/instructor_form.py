from app.forms.base import ModelForm

from .fields import contract_field, enabled_field, name_field, phone_field


class InstructorForm(ModelForm):
    name = name_field()
    phone = phone_field()
    contract = contract_field()
    enabled = enabled_field()
