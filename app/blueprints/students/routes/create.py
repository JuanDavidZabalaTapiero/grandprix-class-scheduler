from flask import redirect, render_template, url_for

from app.blueprints.students import students_bp  # BLUEPRINT
from app.blueprints.students.forms import RegisterStudentForm  # FORM
from app.blueprints.students.services.create_student import (
    CreateStudentInput,
    create_student,
)  # SERVICIO
from app.core.exceptions import AppError
from app.core.transactions import run_service


@students_bp.get("/register")
def register_student_form():

    # GENERAR FORMULARIO
    form = RegisterStudentForm()

    return render_template("students/register.html", form=form)


@students_bp.post("/register")
def register_student():

    # FORM
    form = RegisterStudentForm()

    if not form.validate_on_submit():
        return render_template("students/register.html", form=form)

    # DATOS
    input_data = CreateStudentInput(
        document_id=form.document_id.data,
        name=form.name.data,
        phone=form.phone.data,
    )

    # EJECUTAR SERVICIO
    try:
        run_service(
            lambda: create_student(input_data), "Alumno registrado correctamente"
        )

        return redirect(url_for("students.home"))

    except AppError:
        return render_template("students/register.html", form=form)
