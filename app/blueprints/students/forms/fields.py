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


def document_field():
    return text_field("Nº de documento", max_length=50)
