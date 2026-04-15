from app.forms.base import ModelForm

from .fields import is_default_field, name_field


class LessonTypeForm(ModelForm):
    name = name_field()
    is_default = is_default_field()
