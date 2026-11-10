from flask import Blueprint, render_template

from app.core.transactions import run_query

from .utils import (
    WEEKDAY_COLUMNS,
    get_saturday_pending_students_matrix,
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
