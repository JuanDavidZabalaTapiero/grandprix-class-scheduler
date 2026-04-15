from datetime import time

from flask import Blueprint, flash, jsonify, request

from app.blueprints.instructors.services.crud import instructor_services
from app.core.exceptions import AppError
from app.core.transactions import run_query, run_service

from .services.crud import lesson_services
from .utils.schedule import build_schedule

api_bp = Blueprint("lessons_api", __name__, url_prefix="/api/lessons")


@api_bp.get("/")
def get_schedule():

    try:
        # === DATA ===
        date = request.args.get("date")
        instructors = run_query(lambda: instructor_services.get_available_instructors())
        hours = [time(h, 0, 0) for h in range(6, 22)]

        # === QUERY ===
        lessons = run_query(lambda: lesson_services.get_schedule(date, instructors))

        # === BUILD ===
        lessons_dict = build_schedule(hours, instructors, lessons)

        # === RESPONSE ===
        return jsonify({"data": lessons_dict})

    except AppError as e:
        return jsonify({"message": str(e)}), e.status_code


@api_bp.post("/")
def create_lessons():

    data = request.get_json()

    try:
        # SERVICE
        run_service(lambda: lesson_services.bulk_create(data), show_flash=False)

        # MENSAJE
        flash("Clases agendadas correctamente", "success")

        return jsonify({"message": "Clases agendadas correctamente"}), 201

    except AppError as e:
        return jsonify({"message": str(e)}), e.status_code
