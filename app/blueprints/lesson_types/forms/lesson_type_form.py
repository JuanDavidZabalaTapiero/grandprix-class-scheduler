from app.forms.base import ModelForm

from .fields import name_field


class LessonTypeForm(ModelForm):
    name = name_field()
