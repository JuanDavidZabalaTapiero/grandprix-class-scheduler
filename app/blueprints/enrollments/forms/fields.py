from wtforms import SelectField
from wtforms.validators import DataRequired

from app.forms.fields import text_field


def student_id_field():
    return text_field("ID del estudiate", max_length=50)


def category_id_field():
    return SelectField(
        "Categoría",
        coerce=int,
        validators=[DataRequired(message="Este campo es obligatorio")],
    )
