from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp


class RegisterStudentForm(FlaskForm):
    document_id = StringField(
        "Nº de documento",
        validators=[
            DataRequired(message="El documento es obligatorio"),
            Length(max=50),
            Regexp(
                r"^[0-9A-Za-z\-\.]+$",
                message="El documento solo puede contener letras, números, guiones o puntos",
            ),
        ],
    )

    name = StringField(
        "Nombre completo",
        validators=[
            DataRequired(message="El nombre es obligatorio"),
            Length(min=3, max=255),
        ],
    )

    phone = StringField(
        "Teléfono",
        validators=[
            DataRequired(message="El teléfono es obligatorio"),
            Length(min=7, max=20),
            Regexp(
                r"^[0-9\+\-\s]+$",
                message="El teléfono solo puede contener números, espacios, + o -",
            ),
        ],
    )

    submit = SubmitField("Registrar alumno")
