from datetime import date

from flask import flash, redirect, render_template, request, url_for

from app.blueprints.students import students_bp
from app.blueprints.students.services.details import (
    create_student_medical_exam,
    create_student_note,
    get_student_details,
    update_student_balance,
    update_student_medical_exam,
    update_student_note,
    update_student_preference,
)
from app.core.exceptions import AppError
from app.core.transactions import run_query, run_service


def _run_details_action(student_id, action, success_message):
    try:
        run_service(action, success_message)
    except AppError as error:
        flash(str(error), "danger")

    return redirect(url_for("students.details", student_id=student_id))


@students_bp.get("/<int:student_id>/details")
def details(student_id):
    student_details = run_query(lambda: get_student_details(student_id))

    return render_template(
        "students/details.html",
        **student_details,
    )


@students_bp.post("/<int:student_id>/details/balance")
def update_balance(student_id):
    return _run_details_action(
        student_id,
        lambda: update_student_balance(
            student_id,
            has_balance="has_balance" in request.form,
        ),
        "Saldo del alumno actualizado correctamente",
    )


@students_bp.post("/<int:student_id>/details/preferences")
def update_preferences(student_id):
    return _run_details_action(
        student_id,
        lambda: update_student_preference(
            student_id,
            wants_automatic="wants_automatic" in request.form,
        ),
        "Preferencia actualizada correctamente",
    )


@students_bp.post("/<int:student_id>/details/medical-exams")
def create_medical_exam(student_id):
    exam_date = request.form.get("exam_date", "")
    expiration_date = request.form.get("expiration_date", "")

    if not exam_date or not expiration_date:
        flash("Indica la fecha del examen y su vencimiento.", "warning")
        return redirect(url_for("students.details", student_id=student_id))

    return _run_details_action(
        student_id,
        lambda: create_student_medical_exam(
            student_id,
            date.fromisoformat(exam_date),
            date.fromisoformat(expiration_date),
        ),
        "Examen médico registrado correctamente",
    )


@students_bp.post("/<int:student_id>/details/medical-exams/<int:medical_exam_id>")
def edit_medical_exam(student_id, medical_exam_id):
    exam_date = request.form.get("exam_date", "")
    expiration_date = request.form.get("expiration_date", "")

    if not exam_date or not expiration_date:
        flash("Indica la fecha del examen y su vencimiento.", "warning")
        return redirect(url_for("students.details", student_id=student_id))

    return _run_details_action(
        student_id,
        lambda: update_student_medical_exam(
            student_id,
            medical_exam_id,
            date.fromisoformat(exam_date),
            date.fromisoformat(expiration_date),
        ),
        "Examen médico actualizado correctamente",
    )


@students_bp.post("/<int:student_id>/details/notes")
def create_note(student_id):
    return _run_details_action(
        student_id,
        lambda: create_student_note(
            student_id,
            request.form.get("note", "").strip(),
        ),
        "Nota añadida correctamente",
    )


@students_bp.post("/<int:student_id>/details/notes/<int:note_id>")
def edit_note(student_id, note_id):
    return _run_details_action(
        student_id,
        lambda: update_student_note(
            student_id,
            note_id,
            request.form.get("note", "").strip(),
        ),
        "Nota actualizada correctamente",
    )
