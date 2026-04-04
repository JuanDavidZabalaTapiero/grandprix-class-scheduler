from wtforms import BooleanField

from app.forms.fields import text_field


def license_plate_field():
    return text_field("Placa", max_length=20)


def model_field():
    return text_field("Modelo", max_length=20)


def brand_field():
    return text_field("Marca", max_length=50)


def type_field():
    return text_field("Tipo", max_length=20)


def enabled_field():
    return BooleanField("Activo")
