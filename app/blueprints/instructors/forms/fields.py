from wtforms import BooleanField, StringField
from wtforms.validators import DataRequired, Length, Regexp

from app.forms.normalizers import normalize_name, normalize_phone

# =========================
# NORMALIZADORES
# =========================


def normalize_contract(value: str) -> str:
    if value:
        return value.strip().upper()
    return value


# =========================
# CAMPOS REUTILIZABLES
# =========================


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


def contract_field():
    return StringField(
        "Tipo de contrato",
        validators=[
            DataRequired(message="El tipo de contrato es obligatorio"),
            Length(
                max=50,
                message="El tipo de contrato no puede tener más de %(max)d caracteres",
            ),
        ],
        filters=[normalize_contract],
    )


def enabled_field():
    return BooleanField("Activo")
