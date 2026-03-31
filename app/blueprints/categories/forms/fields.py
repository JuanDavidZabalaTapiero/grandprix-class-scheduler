from wtforms import StringField
from wtforms.validators import DataRequired, Length

from app.forms.normalizers import normalize_name

# =========================
# CAMPOS REUTILIZABLES
# =========================


def name_field():
    return StringField(
        "Nombre",
        validators=[
            DataRequired(message="El nombre es obligatorio"),
            Length(
                min=2,
                max=100,
                message="El nombre debe tener entre %(min)d y %(max)d caracteres",
            ),
        ],
        filters=[normalize_name],
    )
