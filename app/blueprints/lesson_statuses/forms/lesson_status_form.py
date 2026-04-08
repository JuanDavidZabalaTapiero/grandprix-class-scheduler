from app.forms.base import ModelForm

from .fields import name_field


class LessonStatusForm(ModelForm):
    name = name_field()
