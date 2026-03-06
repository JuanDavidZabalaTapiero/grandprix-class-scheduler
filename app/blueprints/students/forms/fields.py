import re

from wtforms import StringField
from wtforms.validators import DataRequired, Length, Regexp

# =========================
# NORMALIZADORES
# =========================


def normalize_document(value: str) -> str:
    if value:
        return value.strip().upper()
    return value


def normalize_name(value: str) -> str:
    if value:
        value = value.strip()
        value = re.sub(r"\s+", " ", value)
        return value.upper()
    return value


def normalize_phone(value: str) -> str:
    if value:
        return value.strip()
    return value


# =========================
# CAMPOS REUTILIZABLES
# =========================


def document_field():
    return StringField(
        "Nº de documento",
        validators=[
            DataRequired(message="El documento es obligatorio"),
            Length(
                max=50, message="El documento no puede tener más de %(max)d caracteres"
            ),
            Regexp(
                r"^[0-9A-Za-z\-\.]+$",
                message="El documento solo puede contener letras, números, guiones o puntos",
            ),
        ],
        filters=[normalize_document],
    )


def name_field():
    return StringField(
        "Nombre completo",
        validators=[
            DataRequired(message="El nombre es obligatorio"),
            Length(
                min=3,
                max=255,
                message="El nombre debe tener entre %(min)d y %(max)d caracteres",
            ),
        ],
        filters=[normalize_name],
    )


def phone_field():
    return StringField(
        "Teléfono",
        validators=[
            DataRequired(message="El teléfono es obligatorio"),
            Length(
                min=7,
                max=20,
                message="El teléfono debe tener entre %(min)d y %(max)d caracteres",
            ),
            Regexp(
                r"^[0-9\+\-\s]+$",
                message="El teléfono solo puede contener números, espacios, + o -",
            ),
        ],
        filters=[normalize_phone],
    )
