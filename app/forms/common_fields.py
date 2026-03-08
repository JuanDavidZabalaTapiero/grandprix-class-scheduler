import re

from wtforms import StringField
from wtforms.validators import DataRequired, Length, Regexp

# =========================
# NORMALIZADORES
# =========================


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


def name_field(label="Nombre completo", min_length=3, max_length=255):
    return StringField(
        label,
        validators=[
            DataRequired(message=f"El {label} es obligatorio"),
            Length(
                min=min_length,
                max=max_length,
                message=f"El {label} debe tener entre %(min)d y %(max)d caracteres",
            ),
        ],
        filters=[normalize_name],
    )


def phone_field(label="Teléfono", min_length=7, max_length=20):
    return StringField(
        label,
        validators=[
            DataRequired(message=f"El {label} es obligatorio"),
            Length(
                min=min_length,
                max=max_length,
                message=f"El {label} debe tener entre %(min)d y %(max)d caracteres",
            ),
            Regexp(
                r"^[0-9\+\-\s]+$",
                message=f"El {label} solo puede contener números, espacios, + o -",
            ),
        ],
        filters=[normalize_phone],
    )
