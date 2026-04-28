from datetime import date

from flask import render_template

from app.blueprints.enrollments import enrollments_bp
from app.blueprints.enrollments.services.crud import enrollment_services
from app.blueprints.instructors.services.crud import instructor_services
from app.blueprints.lesson_statuses.services.crud import lesson_status_services
from app.blueprints.lesson_types.services.crud import lesson_type_services
from app.blueprints.lessons.services.crud import lesson_services
from app.core.transactions import run_query


@enrollments_bp.get("/<int:enrollment_id>")
def home(enrollment_id):

    # FECHA
    today = date.today()

    # MATRÍCULA
    enrollment = run_query(lambda: enrollment_services.get_by_id(enrollment_id))

    # CLASES
    lessons = run_query(lambda: lesson_services.get_lessons(enrollment.id))

    # INSTRUCTORES
    instructors = run_query(lambda: instructor_services.get_available_instructors())

    # === TIPO / ESTADO ===
    lesson_types = run_query(lambda: lesson_type_services.get_all())
    lesson_statuses = run_query(lambda: lesson_status_services.get_all())

    return render_template(
        "enrollments/home.html",
        enrollment=enrollment,
        lessons=lessons,
        today=today,
        instructors=instructors,
        lesson_types=lesson_types,
        lesson_statuses=lesson_statuses,
    )
