from datetime import date

from flask import flash, redirect, render_template, request, url_for

from app.blueprints.availability.utils import (
    WEEKDAY_COLUMNS,
    get_saturday_availability_matrix,
    get_weekday_availability_matrix,
)
from app.blueprints.categories.services.crud import category_services
from app.blueprints.students import students_bp
from app.blueprints.students.exceptions import StudentDocumentAlreadyExists
from app.blueprints.students.services.crud import student_services
from app.core.transactions import run_query, run_service
from app.db.models import (
    Enrollment,
    Student,
    StudentAvailability,
    StudentMedicalExam,
    StudentNote,
    StudentPreference,
)
from app.extensions import db

# ======================================================================
# FUNCIÓN AUXILIAR
# ======================================================================


def _save_student_onboarding(
    *,
    document_id,
    name,
    phone,
    has_balance,
    category_ids,
    availability_block_ids,
    exam_date,
    expiration_date,
    wants_automatic,
    note,
):
    # 1. Registrar alumno
    student = Student(
        document_id=document_id,
        name=name,
        phone=phone,
        has_balance=has_balance,
    )
    db.session.add(student)
    db.session.flush()  # Obtiene student.id sin confirmar la transacción.

    # 2. Registrar matrículas seleccionadas
    for category_id in category_ids:
        db.session.add(
            Enrollment(
                student_id=student.id,
                category_id=category_id,
            )
        )

    # 3. Registrar horarios disponibles seleccionados
    for block_id in availability_block_ids:
        db.session.add(
            StudentAvailability(
                student_id=student.id,
                availability_block_id=block_id,
            )
        )

    # 4. Registrar examen médico si se enviaron ambas fechas
    if exam_date and expiration_date:
        db.session.add(
            StudentMedicalExam(
                student_id=student.id,
                exam_date=date.fromisoformat(exam_date),
                expiration_date=date.fromisoformat(expiration_date),
            )
        )

    # 5. Registrar preferencia, incluso si wants_automatic es False
    db.session.add(
        StudentPreference(
            student_id=student.id,
            wants_automatic=wants_automatic,
        )
    )

    # 6. Registrar nota si tiene contenido
    if note:
        db.session.add(
            StudentNote(
                student_id=student.id,
                note=note,
            )
        )

    return student


# ======================================================================
# ENDPOINTS
# ======================================================================


@students_bp.get("/onboarding")
def onboarding_form():
    categories = run_query(lambda: category_services.get_all())
    weekday_matrix = run_query(get_weekday_availability_matrix)
    saturday_matrix = run_query(get_saturday_availability_matrix)

    weekday_columns = [
        (day_name, column_key) for _, day_name, column_key in WEEKDAY_COLUMNS
    ]

    return render_template(
        "students/onboarding.html",
        categories=categories,
        weekday_matrix=weekday_matrix,
        weekday_columns=weekday_columns,
        saturday_matrix=saturday_matrix,
    )


@students_bp.post("/onboarding")
def onboarding():
    category_ids = [
        int(category_id) for category_id in request.form.getlist("category_ids")
    ]
    availability_block_ids = [
        int(block_id) for block_id in request.form.getlist("availability_block_ids")
    ]

    exam_date = request.form.get("exam_date", "").strip()
    expiration_date = request.form.get("expiration_date", "").strip()
    note = request.form.get("student_note", "").strip()

    try:
        run_service(
            lambda: _save_student_onboarding(
                document_id=request.form.get("student_document_id"),
                name=request.form.get("student_name"),
                phone=request.form.get("student_phone"),
                has_balance="student_has_balance" in request.form,
                category_ids=category_ids,
                availability_block_ids=availability_block_ids,
                exam_date=exam_date,
                expiration_date=expiration_date,
                wants_automatic="wants_automatic" in request.form,
                note=note,
            ),
            "Alumno registrado correctamente",
            unique_fields=student_services.unique_fields,
        )

    except StudentDocumentAlreadyExists as error:
        flash(str(error), "danger")

    return redirect(url_for("students.onboarding_form"))
