from app.forms.base import ModelForm

from .fields import (
    brand_field,
    enabled_field,
    license_plate_field,
    model_field,
    type_field,
)


class VehicleForm(ModelForm):
    license_plate = license_plate_field()
    model = model_field()
    brand = brand_field()
    type = type_field()
    enabled = enabled_field()
