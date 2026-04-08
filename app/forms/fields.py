from wtforms import SelectField, StringField
from wtforms.validators import DataRequired, Length, Optional

from app.forms.normalizers import normalize_text

# === STRINGS ===


def text_field(
    label,
    *,
    min_length=1,
    max_length=None,
    required=True,
    filters=None,
    extra_validators=None,
):
    validators = []
    filters = [normalize_text]

    # DATA REQUIRED
    if required:
        validators.append(DataRequired(message="Este campo es obligatorio"))
    else:
        validators.append(Optional())

    # LENGTH
    if max_length is not None:
        validators.append(
            Length(
                min=min_length,
                max=max_length,
                message=f"Este campo debe tener entre {min_length} y {max_length} caracteres",
            )
        )

    # EXTRA VALIDATORS
    if extra_validators:
        validators.extend(extra_validators)

    return StringField(label, validators=validators, filters=filters)


# === SELECT ===


def select_field(label, *, required=True, coerce=int):
    validators = []

    # DATA REQUIRED
    if required:
        validators.append(DataRequired(message="Este campo es obligatorio"))
    else:
        validators.append(Optional())

    return SelectField(label, coerce=coerce, validators=validators)
