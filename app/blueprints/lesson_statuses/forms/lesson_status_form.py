from app.forms.base import ModelForm

from .fields import is_default_field, name_field, show_in_scheduling_field


class LessonStatusForm(ModelForm):
    name = name_field()
    show_in_scheduling = show_in_scheduling_field()
    is_default = is_default_field()
