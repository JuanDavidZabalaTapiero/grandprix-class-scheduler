from flask import redirect, render_template, url_for

from app.blueprints.students import students_bp  # BLUEPRINT
from app.blueprints.students.forms.edit_student_form import EditStudentForm  # FORM

# SERVICIOS
from app.blueprints.students.services.get_student import get_student_by_id
from app.blueprints.students.services.update_student import (
    UpdateStudentInput,
    update_student,
)
from app.core.exceptions import AppError
from app.core.transactions import run_service


@students_bp.get("/<int:student_id>/edit")
def edit_student_form(student_id):

    # CONSULTAR ALUMNO
    student = get_student_by_id(student_id)

    # GENERAR FORMULARIO
    form = EditStudentForm(obj=student)

    return render_template("students/edit.html", form=form, student=student)


@students_bp.post("/<int:student_id>/edit")
def edit_student(student_id):

    # CONSULTAR ALUMNO
    student = get_student_by_id(student_id)

    # FORM
    form = EditStudentForm()

    if not form.validate_on_submit():
        return render_template("students/edit.html", form=form, student=student)

    # DATOS
    input_data = UpdateStudentInput(
        student=student,
        document_id=form.document_id.data,
        name=form.name.data,
        phone=form.phone.data,
    )

    # EJECUTAR SERVICIO
    try:
        run_service(
            lambda: update_student(input_data), "Alumno actualizado correctamente"
        )

        return redirect(url_for("students.home"))

    except AppError:
        return render_template("students/edit.html", form=form, student=student)
