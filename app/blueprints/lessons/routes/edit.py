from flask import flash, redirect, render_template, request, url_for

from app.blueprints.instructor_vehicles.services.crud import instructor_vehicle_services
from app.blueprints.lessons import lessons_bp
from app.blueprints.lessons.services.crud import lesson_services
from app.blueprints.lessons.utils.vehicle_conflict import is_vehicle_busy
from app.core.transactions import run_query, run_service
from app.extensions import db


@lessons_bp.get("/<int:lesson_id>/edit")
def edit_lesson_form(lesson_id):

    lesson = run_query(lambda: lesson_services.get_by_id(lesson_id))
    active_instructor_vehicles = [
        iv
        for iv in lesson.instructor_vehicle.instructor.instructor_vehicles
        if iv.vehicle.enabled
    ]

    return render_template(
        "lessons/edit.html",
        lesson=lesson,
        active_instructor_vehicles=active_instructor_vehicles,
    )


@lessons_bp.post("/<int:lesson_id>/edit")
def edit_lesson(lesson_id):

    lesson = run_query(lambda: lesson_services.get_by_id(lesson_id))

    # DATA
    new_instructor_vehicle_id = int(request.form.get("instructor_vehicle_id"))
    notes = request.form.get("notes")

    # GUARDAR NOTA
    lesson.notes = notes
    db.session.commit()

    # GUARDAR INSTRUCTOR-VEHICLE
    if new_instructor_vehicle_id != lesson.instructor_vehicle_id:
        new_instructor_vehicle = run_query(
            lambda: instructor_vehicle_services.get_by_id(new_instructor_vehicle_id)
        )
        vehicle_id = new_instructor_vehicle.vehicle_id

        if is_vehicle_busy(vehicle_id, lesson):
            flash("Ese vehículo ya está ocupado en ese horario", "danger")
            return redirect(url_for("lessons.edit_lesson_form", lesson_id=lesson_id))

        lesson.instructor_vehicle_id = new_instructor_vehicle_id
        db.session.commit()

    flash("Clase editada correctamente", "success")

    return redirect(url_for("lessons.edit_lesson_form", lesson_id=lesson_id))


# === UPDATE STATUS ===
@lessons_bp.get("/<int:enrollment_id>/update/status")
def update_status(enrollment_id):
    run_service(
        lambda: lesson_services.update_lesson_status(enrollment_id),
        "Clases actualizadas correctamente",
    )
    return redirect(url_for("enrollments.home", enrollment_id=enrollment_id))


@lessons_bp.get("/all/update/status")
def update_all_status():
    run_service(
        lambda: lesson_services.update_all_lessons_status(),
        "Clases actualizadas correctamente",
    )
    return redirect(url_for("students.home"))
