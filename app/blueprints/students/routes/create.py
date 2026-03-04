from flask import flash, redirect, render_template, url_for

from app.blueprints.students import students_bp  # BLUEPRINT
from app.blueprints.students.forms import RegisterStudentForm  # FORM
from app.blueprints.students.services.create_student import (
    CreateStudentInput,
    create_student,
)  # SERVICIO
from app.core.exceptions import AppError
from app.extensions import db


@students_bp.get("/register")
def register_student_form():

    # GENERAR FORMULARIO
    form = RegisterStudentForm()

    return render_template("students/register.html", form=form)


@students_bp.post("/register")
def register_student():

    # CAPTURAR FORMULARIO (DATOS)
    form = RegisterStudentForm()

    # VALIDACIÓN: ERROR
    if not form.validate_on_submit():
        return render_template("students/register.html", form=form)

    # VALIDACIÓN: OK
    try:
        input_data = CreateStudentInput(
            document_id=form.document_id.data,
            name=form.name.data,
            phone=form.phone.data,
        )

        # COMMIT
        create_student(input_data)
        db.session.commit()

        # MENSAJE
        flash("Alumno registrado correctamente", "success")

        return redirect(url_for("students.home"))

    # ERROR
    except AppError as e:
        db.session.rollback()
        flash(str(e), "danger")

    return render_template("students/register.html", form=form)
