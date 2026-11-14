from datetime import date, time

from flask import flash, redirect, render_template, request, url_for

from app.blueprints.blocked_days.services import (
    create_blocked_slot,
    delete_blocked_slot,
    get_all_future_blocked_slots,
)
from app.blueprints.instructors import instructors_bp
from app.blueprints.instructors.services.crud import instructor_services
from app.core.exceptions import AppError
from app.core.transactions import run_query, run_service


# LIST
@instructors_bp.get("/block-slot")
def block_slot_home():
    blocked_slots = run_query(get_all_future_blocked_slots)
    instructors = run_query(instructor_services.get_all_active_instructors)

    hours = [time(hour, 0) for hour in range(6, 22)]

    return render_template(
        "instructors/block_slot/home.html",
        blocked_slots=blocked_slots,
        instructors=instructors,
        hours=hours,
    )


# CREATE
@instructors_bp.post("/block-slot")
def register_blocked_slot():
    try:
        block_date = date.fromisoformat(request.form.get("date", ""))
        start_time = time.fromisoformat(request.form.get("start_time", ""))
        instructor_id = int(request.form.get("instructor_id", ""))
    except (TypeError, ValueError):
        flash("Indica una fecha, hora e instructor válidos.", "danger")
        return redirect(url_for("instructors.block_slot_home"))

    try:
        run_service(
            lambda: create_blocked_slot(
                block_date,
                instructor_id,
                start_time,
            ),
            "Bloque horario registrado correctamente",
        )
    except AppError as error:
        flash(str(error), "danger")

    return redirect(url_for("instructors.block_slot_home"))


# DELETE
@instructors_bp.post("/block-slot/<int:blocked_slot_id>/delete")
def delete_blocked_slot_route(blocked_slot_id):
    try:
        run_service(
            lambda: delete_blocked_slot(blocked_slot_id),
            "Bloque horario eliminado correctamente",
        )
    except AppError as error:
        flash(str(error), "danger")

    return redirect(url_for("instructors.block_slot_home"))
