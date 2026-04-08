from app.forms.base import ModelForm

from .fields import instructor_id_field, vehicle_id_field


class InstructorVehicleForm(ModelForm):
    instructor_id = instructor_id_field()
    vehicle_id = vehicle_id_field()
