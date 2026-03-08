from wtforms import BooleanField, StringField
from wtforms.validators import DataRequired, Length

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


def contract_field():
    return StringField(
        "Tipo de contrato",
        validators=[
            DataRequired(message="El tipo de contrato es obligatorio"),
            Length(
                max=50,
                message="El contrato no puede tener más de %(max)d caracteres",
            ),
        ],
        filters=[normalize_contract],
    )


def enabled_field():
    return BooleanField("Instructor activo")
