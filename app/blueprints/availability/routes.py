from flask import Blueprint, redirect, render_template, request, url_for

from app.blueprints.students.services.crud import student_services
from app.core.transactions import run_query, run_service

from .services import replace_student_availabilities
from .utils import (
    WEEKDAY_COLUMNS,
    get_saturday_pending_students_matrix,
    get_student_saturday_availability_matrix,
    get_student_weekday_availability_matrix,
    get_weekday_pending_students_matrix,
)

availability_bp = Blueprint(
    "availability",
    __name__,
    url_prefix="/availability",
)


@availability_bp.get("/planning")
def planning():
    weekday_matrix = run_query(get_weekday_pending_students_matrix)
    saturday_matrix = run_query(get_saturday_pending_students_matrix)

    weekday_columns = [
        (day_name, column_key) for _, day_name, column_key in WEEKDAY_COLUMNS
    ]

    return render_template(
        "availability/planning.html",
        weekday_matrix=weekday_matrix,
        weekday_columns=weekday_columns,
        saturday_matrix=saturday_matrix,
    )


@availability_bp.get("/students/<int:student_id>")
def student_schedule(student_id):
    student = run_query(lambda: student_services.get_by_id(student_id))
    weekday_matrix = run_query(
        lambda: get_student_weekday_availability_matrix(student_id)
    )
    saturday_matrix = run_query(
        lambda: get_student_saturday_availability_matrix(student_id)
    )

    weekday_columns = [
        (day_name, column_key) for _, day_name, column_key in WEEKDAY_COLUMNS
    ]

    return render_template(
        "availability/student_schedule.html",
        student=student,
        weekday_matrix=weekday_matrix,
        weekday_columns=weekday_columns,
        saturday_matrix=saturday_matrix,
    )


@availability_bp.route(
    "/students/<int:student_id>/edit",
    methods=["GET", "POST"],
)
def edit_student_schedule(student_id):
    student = run_query(lambda: student_services.get_by_id(student_id))

    if request.method == "POST":
        selected_block_ids = [
            int(block_id) for block_id in request.form.getlist("availability_block_ids")
        ]

        run_service(
            lambda: replace_student_availabilities(
                student_id,
                selected_block_ids,
            ),
            "Horarios actualizados correctamente",
        )

        return redirect(
            url_for(
                "availability.student_schedule",
                student_id=student_id,
            )
        )

    weekday_matrix = run_query(
        lambda: get_student_weekday_availability_matrix(student_id)
    )
    saturday_matrix = run_query(
        lambda: get_student_saturday_availability_matrix(student_id)
    )
    weekday_columns = [
        (day_name, column_key) for _, day_name, column_key in WEEKDAY_COLUMNS
    ]

    return render_template(
        "availability/edit_student_schedule.html",
        student=student,
        weekday_matrix=weekday_matrix,
        weekday_columns=weekday_columns,
        saturday_matrix=saturday_matrix,
    )
