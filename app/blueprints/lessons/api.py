from datetime import time

from flask import Blueprint, flash, jsonify, request

from app.blueprints.instructors.services.crud import instructor_services
from app.core.exceptions import AppError
from app.core.transactions import run_query, run_service

from .services.crud import lesson_services
from .utils.scheduling import build_scheduling

api_bp = Blueprint("lessons_api", __name__, url_prefix="/api/lessons")


@api_bp.get("/")
def get_schedule():

    try:
        # === DATA ===
        date = request.args.get("date")
        instructors = run_query(lambda: instructor_services.get_available_instructors())
        hours = [time(h, 0, 0) for h in range(6, 22)]

        # === QUERY ===
        lessons, totals = run_query(
            lambda: lesson_services.get_schedule(date, instructors)
        )

        # === BUILD ===
        lessons_dict = build_scheduling(hours, instructors, lessons)

        # === RESPONSE ===
        return jsonify({"lessons": lessons_dict, "totals": totals})

    except AppError as e:
        return jsonify({"message": str(e)}), e.status_code


@api_bp.post("/")
def create_lessons():

    data = request.get_json()

    try:
        # CREATE + ORGANIZE
        def service():
            lesson_services.bulk_create(data)
            lesson_services.organize_lesson_number(data["enrollment_id"])

        run_service(service, show_flash=False)

        # MENSAJE
        flash("Clases agendadas correctamente", "success")

        return jsonify({"message": "Clases agendadas correctamente"}), 201

    except AppError as e:
        return jsonify({"message": str(e)}), e.status_code


@api_bp.put("/")
def update_lessons():

    data = request.get_json()

    try:

        # UPDATE
        for lesson_data in data["lessons"]:
            lesson = lesson_services.get_by_id(lesson_data["id"])

            for field, value in lesson_data.items():
                if field != "id":
                    setattr(lesson, field, value)

        # ORGANIZE
        run_service(
            lambda: lesson_services.organize_lesson_number(data["enrollment_id"]),
            show_flash=False,
        )

        # MENSAJE
        flash("Clases actualizadas correctamente", "success")

        return jsonify({"message": "Clases actualizadas correctamente"}), 201

    except AppError as e:
        return jsonify({"message": str(e)}), e.status_code


@api_bp.post("/delete")
def delete_lessons():

    data = request.get_json()

    try:
        # DELETE + ORGANIZE
        def service():
            lesson_services.bulk_delete(data["lessons"])
            lesson_services.organize_lesson_number(data["enrollment_id"])

        run_service(service, show_flash=False)

        # MENSAJE
        flash("Clases eliminadas correctamente", "success")

        return jsonify({"message": "Clases eliminadas correctamente"}), 201

    except AppError as e:
        return jsonify({"message": str(e)}), e.status_code


@api_bp.post("/change")
def change_lessons():

    data = request.get_json()

    try:

        def service():

            for selection in data:

                origin_id = selection["originId"]
                target = selection["target"]

                lesson_origin = lesson_services.get_by_id(origin_id)

                # =========================
                # CAMBIO ENTRE CLASES
                # =========================
                if isinstance(target, int):

                    lesson_target = lesson_services.get_by_id(target)

                    # GUARDAR TEMP
                    temp_date = lesson_origin.date
                    temp_time = lesson_origin.start_time
                    temp_iv = lesson_origin.instructor_vehicle_id

                    # SWAP
                    lesson_origin.date = lesson_target.date
                    lesson_origin.start_time = lesson_target.start_time
                    lesson_origin.instructor_vehicle_id = (
                        lesson_target.instructor_vehicle_id
                    )

                    lesson_target.date = temp_date
                    lesson_target.start_time = temp_time
                    lesson_target.instructor_vehicle_id = temp_iv

                    # ORGANIZE
                    lesson_services.organize_lesson_number(lesson_origin.enrollment_id)
                    lesson_services.organize_lesson_number(lesson_target.enrollment_id)

                # =========================
                # MOVER A SLOT VACÍO
                # =========================
                elif isinstance(target, dict):

                    lesson_origin.date = target["date"]
                    lesson_origin.start_time = target["hour"]
                    lesson_origin.instructor_vehicle_id = target[
                        "instructor_vehicle_id"
                    ]

                    lesson_services.organize_lesson_number(lesson_origin.enrollment_id)

                else:
                    raise AppError("Formato de target inválido", 400)

        # UNA SOLA TRANSACCIÓN
        run_service(service, show_flash=False)

        flash("Cambios realizados correctamente", "success")

        return jsonify({"message": "Cambios realizados correctamente"}), 201

    except AppError as e:
        return jsonify({"message": str(e)}), e.status_code
