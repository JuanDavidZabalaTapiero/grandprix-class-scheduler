import logging

from flask import flash, redirect, render_template, url_for

from app.blueprints.students import students_bp  # BLUEPRINT
from app.blueprints.students.exceptions import StudentError
from app.blueprints.students.forms import RegisterStudentForm  # FORMULARIO
from app.blueprints.students.services.create_student import (
    CreateStudentInput,
    create_student,
)  # SERVICIO
from app.db.exceptions import DatabaseConnectionError

logger = logging.getLogger(__name__)


@students_bp.get("/register")
def register_student_form():
    form = RegisterStudentForm()

    return render_template("students/register.html", form=form)


@students_bp.post("/register")
def register_student():
    form = RegisterStudentForm()

    # VALIDACIÓN (ERROR)
    if not form.validate_on_submit():
        return render_template("students/register.html", form=form)

    # VALIDACIÓN (OK) -> MANEJAR REGISTRO
    try:
        input_data = CreateStudentInput(
            document_id=form.document_id.data,
            name=form.name.data,
            phone=form.phone.data,
        )

        create_student(input_data)

        flash("Alumno registrado correctamente", "success")

        # VIEW: HOME
        return redirect(url_for("students.home"))

    except DatabaseConnectionError as e:
        flash(str(e), "danger")

    except StudentError as e:
        flash(str(e), "danger")

    except Exception:
        logger.exception("Unexpected error while registering student")
        flash("Error inesperado del sistema. Vuelva a intentar más tarde", "danger")

    # VIEW: REGISTRO + FORM
    return render_template("students/register.html", form=form)
