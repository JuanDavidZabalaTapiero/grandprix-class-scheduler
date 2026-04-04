from wtforms import BooleanField
from wtforms.validators import Regexp

from app.forms.fields import text_field


def name_field():
    return text_field("Nombre completo", max_length=255)


def phone_field():
    return text_field(
        "Teléfono",
        min_length=7,
        max_length=20,
        extra_validators=[
            Regexp(
                r"^[0-9\+\-\s]+$",
                message="El teléfono solo puede contener números, espacios, + o -",
            )
        ],
    )


def contract_field():
    return text_field("Tipo de contrato", max_length=50)


def enabled_field():
    return BooleanField("Activo")
