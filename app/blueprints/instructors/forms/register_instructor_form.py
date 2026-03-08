from app.forms.base import ModelForm
from app.forms.common_fields import name_field, phone_field

from .fields import contract_field, enabled_field


class RegisterInstructorForm(ModelForm):
    name = name_field()
    phone = phone_field()
    contract = contract_field()
    enabled = enabled_field()
