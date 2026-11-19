from datetime import date

from flask import render_template

from app.blueprints.enrollments import enrollments_bp
from app.blueprints.enrollments.services.crud import enrollment_services
from app.blueprints.instructors.services.crud import instructor_services
from app.blueprints.lesson_statuses.services.crud import lesson_status_services
from app.blueprints.lesson_types.services.crud import lesson_type_services
from app.blueprints.lessons.services.crud import lesson_services
from app.core.transactions import run_query
from app.db.models import (
    AvailabilityBlock,
    AvailabilityTimeSlot,
    StudentAvailability,
)
from app.extensions import db


@enrollments_bp.get("/<int:enrollment_id>")
def home(enrollment_id):

    # FECHA
    today = date.today()

    # MATRÍCULA
    enrollment = run_query(lambda: enrollment_services.get_by_id(enrollment_id))

    # DISPONIBILIDAD DEL ALUMNO
    student_availability = run_query(
        lambda: (
            db.session.query(
                AvailabilityBlock.weekday,
                AvailabilityTimeSlot.start_time,
                AvailabilityTimeSlot.end_time,
            )
            .join(
                StudentAvailability,
                StudentAvailability.availability_block_id == AvailabilityBlock.id,
            )
            .join(
                AvailabilityTimeSlot,
                AvailabilityTimeSlot.id == AvailabilityBlock.time_slot_id,
            )
            .filter(
                StudentAvailability.student_id == enrollment.student.id,
                AvailabilityBlock.enabled.is_(True),
            )
            .all()
        )
    )

    # CLASES
    lessons = run_query(lambda: lesson_services.get_lessons(enrollment.id))

    # INSTRUCTORES
    instructors = run_query(lambda: instructor_services.get_available_instructors())

    # === TIPO / ESTADO ===
    lesson_types = run_query(lambda: lesson_type_services.get_all())
    lesson_statuses = run_query(lambda: lesson_status_services.get_all())

    availability_by_day = {}

    for weekday, start_time, end_time in student_availability:
        availability_by_day.setdefault(weekday, []).append(
            {
                "start": start_time.strftime("%H:%M"),
                "end": end_time.strftime("%H:%M"),
            }
        )

    return render_template(
        "enrollments/home.html",
        enrollment=enrollment,
        lessons=lessons,
        today=today,
        instructors=instructors,
        lesson_types=lesson_types,
        lesson_statuses=lesson_statuses,
        availability_by_day=availability_by_day,
    )
