from wtforms import StringField
from wtforms.validators import DataRequired, Length, Regexp

# =========================
# NORMALIZADORES
# =========================


def normalize_document(value: str) -> str:
    if value:
        return value.strip().upper()
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
