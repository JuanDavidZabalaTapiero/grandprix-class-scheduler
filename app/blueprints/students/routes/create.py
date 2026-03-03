from flask import flash, redirect, render_template, url_for

from app.blueprints.students import students_bp  # BLUEPRINT
from app.blueprints.students.forms import RegisterStudentForm  # FORMULARIO
from app.blueprints.students.services.create_student import (
    CreateStudentInput,
    create_student,
)  # SERVICIO
from app.core.exceptions import AppError
from app.extensions import db


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

        # COMMIT
        with db.session.begin():
            create_student(input_data)

        flash("Alumno registrado correctamente", "success")

        # VIEW: HOME
        return redirect(url_for("students.home"))

    except AppError as e:
        flash(str(e), "danger")

    # VIEW: REGISTRO + FORM
    return render_template("students/register.html", form=form)
