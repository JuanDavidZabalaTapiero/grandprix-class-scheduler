from wtforms import BooleanField

from app.forms.fields import text_field


def name_field():
    return text_field("Nombre", max_length=20)


def is_default_field():
    return BooleanField("Default")
