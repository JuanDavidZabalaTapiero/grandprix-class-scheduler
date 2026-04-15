from app.forms.base import ModelForm

from .fields import is_default_field, name_field, show_in_schedule_field


class LessonStatusForm(ModelForm):
    name = name_field()
    show_in_schedule = show_in_schedule_field()
    is_default = is_default_field()
