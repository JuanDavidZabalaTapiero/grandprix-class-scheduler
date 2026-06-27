from flask import flash, redirect, render_template, request, url_for

from app.blueprints.blocked_days.exceptions import BlockedDayAlreadyExists
from app.blueprints.blocked_days.services import (
    create_blocked_day,
    delete_blocked_day,
    get_all_future_blocked_days,
)
from app.blueprints.instructors import instructors_bp
from app.blueprints.instructors.services.crud import instructor_services
from app.core.exceptions import AppError
from app.core.transactions import run_query, run_service


# LIST
@instructors_bp.get("/block-day")
def block_day_home():
    blocked_days = run_query(lambda: get_all_future_blocked_days())
    instructors = run_query(lambda: instructor_services.get_all_active_instructors())
    return render_template(
        "instructors/block_day/home.html",
        blocked_days=blocked_days,
        instructors=instructors,
    )


# CREATE
@instructors_bp.post("/block-day")
def register_blocked_day():

    date = request.form.get("date")
    instructor_id = request.form.get("instructor_id")

    try:
        run_service(
            lambda: create_blocked_day(date, instructor_id),
            "Día bloqueado correctamente",
            unique_fields={"day_and_instructor": BlockedDayAlreadyExists},
        )

    except AppError as e:
        flash(str(e), "danger")

    return redirect(url_for("instructors.block_day_home"))


# DELETE
@instructors_bp.post("/block-day/<int:blocked_day_id>/delete")
def delete_blocked_day_route(blocked_day_id):

    try:
        run_service(
            lambda: delete_blocked_day(blocked_day_id),
            "Día bloqueado eliminado correctamente",
        )

    except AppError as e:
        flash(str(e), "danger")

    return redirect(url_for("instructors.block_day_home"))
