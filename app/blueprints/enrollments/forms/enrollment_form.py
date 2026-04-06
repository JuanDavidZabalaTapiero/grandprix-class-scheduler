from app.forms.base import ModelForm

from .fields import category_id_field, student_id_field


class EnrollmentForm(ModelForm):
    student_id = student_id_field()
    category_id = category_id_field()
