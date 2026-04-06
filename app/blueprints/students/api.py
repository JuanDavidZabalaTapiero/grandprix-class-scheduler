import logging

from flask import Blueprint, jsonify, request

from app.blueprints.students.services.search_students import search_students
from app.core.exceptions import AppError
from app.core.transactions import run_query

logger = logging.getLogger(__name__)

api_bp = Blueprint("students_api", __name__, url_prefix="/api/students")


@api_bp.get("")
def get_students():
    term = request.args.get("search", "")

    try:
        students = run_query(lambda: search_students(term))
        data = [
            {
                "id": student.id,
                "document_id": student.document_id,
                "name": student.name,
                "enrollments": [
                    {"id": e.id, "category": e.category.name}
                    for e in student.enrollments
                ],
            }
            for student in students
        ]
        return jsonify({"data": data}), 200

    except AppError as e:
        return jsonify({"message": str(e)}), e.status_code
