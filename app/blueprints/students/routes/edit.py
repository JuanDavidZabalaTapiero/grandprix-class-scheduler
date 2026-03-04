from flask import flash, redirect, render_template, url_for

from app.blueprints.students import students_bp  # BLUEPRINT
from app.blueprints.students.forms.edit_student_form import EditStudentForm  # FORM

# SERVICIOS
from app.blueprints.students.services.get_student import get_student_by_id
from app.blueprints.students.services.update_student import (
    UpdateStudentInput,
    update_student,
)
from app.core.exceptions import AppError
from app.extensions import db


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

    # CAPTURAR FORMULARIO (DATOS)
    form = EditStudentForm()

    # VALIDACIÓN: ERROR
    if not form.validate_on_submit():
        return render_template("students/edit.html", form=form, student=student)

    # VALIDACIÓN: OK
    try:
        input_data = UpdateStudentInput(
            student=student,
            document_id=form.document_id.data,
            name=form.name.data,
            phone=form.phone.data,
        )

        # COMMIT
        update_student(input_data)
        db.session.commit()

        # MENSAJE
        flash("Alumno actualizado correctamente", "success")

        return redirect(url_for("students.home"))

    # ERROR
    except AppError as e:
        db.session.rollback()
        flash(str(e), "danger")

    return render_template("students/edit.html", form=form, student=student)
