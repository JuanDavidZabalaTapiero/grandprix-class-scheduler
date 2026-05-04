from flask import render_template

from app.blueprints.enrollments.services.crud import enrollment_services
from app.blueprints.lessons import lessons_bp
from app.blueprints.lessons.utils.schedule import build_schedule
from app.blueprints.students.services.crud import student_services
from app.core.transactions import run_query


@lessons_bp.get("/schedule/<int:enrollment_id>")
def schedule(enrollment_id):

    enrollment = run_query(lambda: enrollment_services.get_by_id(enrollment_id))
    schedule_array, total_lessons = build_schedule(enrollment_id=enrollment_id)

    return render_template(
        "lessons/schedule.html",
        enrollment=enrollment,
        schedule_array=schedule_array,
        total_lessons=total_lessons,
    )


@lessons_bp.get("/complete-schedule/<int:student_id>")
def complete_schedule(student_id):

    student = run_query(lambda: student_services.get_by_id(student_id))
    schedule_array, total_lessons = build_schedule(student_id=student_id)

    return render_template(
        "lessons/complete_schedule.html",
        student=student,
        schedule_array=schedule_array,
        total_lessons=total_lessons,
    )
