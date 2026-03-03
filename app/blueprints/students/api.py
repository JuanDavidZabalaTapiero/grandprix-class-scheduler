import logging

from flask import Blueprint, jsonify, request

from app.blueprints.students.services.search_students import search_students
from app.core.exceptions import AppError

logger = logging.getLogger(__name__)

api_bp = Blueprint("students_api", __name__, url_prefix="/api/students")


@api_bp.get("")
def get_students():
    term = request.args.get("search", "")

    try:
        students = search_students(term)
        data = [
            {"id": s.id, "document_id": s.document_id, "name": s.name} for s in students
        ]
        return jsonify({"data": data}), 200

    except AppError as e:
        return jsonify({"message": str(e)}), e.status_code
