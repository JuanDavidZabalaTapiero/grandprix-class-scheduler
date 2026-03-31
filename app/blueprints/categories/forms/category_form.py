from app.forms.base import ModelForm

from .fields import name_field


class CategoryForm(ModelForm):
    name = name_field()
