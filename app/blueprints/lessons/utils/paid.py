from collections import defaultdict
from datetime import timedelta

from sqlalchemy import and_, case, func, select

from app.blueprints.instructors.services.crud import instructor_services
from app.db.models import (
    Category,
    Enrollment,
    Instructor,
    InstructorVehicle,
    Lesson,
    LessonStatus,
    Student,
)
from app.extensions import db


def instructor_report(start_date, end_date):

    instructors = instructor_services.get_all_active_instructors()

    # =========================================================
    # QUERYS
    # =========================================================

    stmt = (
        select(
            Lesson.date.label("date"),
            Instructor.id.label("instructor_id"),
            Instructor.name.label("instructor_name"),
            func.count(Lesson.id).label("total_lessons"),
            func.max(case((Lesson.start_time == "21:00:00", 1), else_=0)).label(
                "has_21_lesson"
            ),
        )
        .join(InstructorVehicle, Lesson.instructor_vehicle_id == InstructorVehicle.id)
        .join(Instructor, InstructorVehicle.instructor_id == Instructor.id)
        .where(
            and_(
                Lesson.is_paid,
                Lesson.date >= start_date,
                Lesson.date <= end_date,
                Instructor.enabled,
            )
        )
        .group_by(Lesson.date, Instructor.id, Instructor.name)
    )

    details_stmt = (
        select(
            Lesson.id,
            Lesson.date,
            Lesson.start_time,
            Lesson.lesson_number,
            Instructor.id.label("instructor_id"),
            Instructor.name.label("instructor_name"),
            LessonStatus.name.label("lesson_status"),
            Student.name.label("student_name"),
            Category.name.label("category_name"),
        )
        .join(InstructorVehicle, Lesson.instructor_vehicle_id == InstructorVehicle.id)
        .join(Instructor, InstructorVehicle.instructor_id == Instructor.id)
        .join(LessonStatus, Lesson.lesson_status_id == LessonStatus.id)
        .join(Enrollment, Lesson.enrollment_id == Enrollment.id)
        .join(Student, Enrollment.student_id == Student.id)
        .join(Category, Enrollment.category_id == Category.id)
        .where(
            and_(
                Lesson.is_paid,
                Lesson.date >= start_date,
                Lesson.date <= end_date,
                Instructor.enabled,
            )
        )
        .order_by(Lesson.date, Lesson.start_time)
    )

    # =========================================================
    # ESTRUCTURAS AUXILIARES
    # =========================================================

    # HORAS
    rows = db.session.execute(stmt).all()

    report_map = {}

    for row in rows:

        report_map[(row.date, row.instructor_id)] = {
            "total_lessons": row.total_lessons,
            "has_21_lesson": bool(row.has_21_lesson),
        }

    # CLASES
    details_rows = db.session.execute(details_stmt).all()

    lessons_map = defaultdict(list)

    for row in details_rows:

        lessons_map[(row.date, row.instructor_id)].append(
            {
                "id": row.id,
                "lesson_number": row.lesson_number,
                "start_time": row.start_time.strftime("%H:%M"),
                "student": row.student_name,
                "category": row.category_name,
                "lesson_status": row.lesson_status,
            }
        )

    # =========================================================
    # GENERAR RANGO DE FECHAS
    # =========================================================

    current_date = start_date

    days = []

    while current_date <= end_date:
        days.append(current_date)
        current_date += timedelta(days=1)

    # =========================================================
    # lessons_per_day
    # =========================================================

    lessons_per_day = []

    for day in days:

        instructors_data = []

        for instructor in instructors:

            data = report_map.get(
                (day, instructor.id), {"total_lessons": 0, "has_21_lesson": False}
            )

            instructors_data.append(
                {
                    "id": instructor.id,
                    "name": instructor.name,
                    "total_paid_lessons": data["total_lessons"],
                    "lessons": lessons_map.get((day, instructor.id), []),
                }
            )

        lessons_per_day.append({"date": str(day), "instructors": instructors_data})

    # =========================================================
    # night_hours
    # =========================================================

    night_hours_map = defaultdict(int)

    for (_date, instructor_id), data in report_map.items():

        qualifies = data["has_21_lesson"] and data["total_lessons"] >= 8

        if qualifies:
            night_hours_map[instructor_id] += 1

    night_hours = []

    for instructor in instructors:

        night_hours.append(
            {
                "instructor_id": instructor.id,
                "night_hours": night_hours_map[instructor.id],
            }
        )

    # =========================================================
    # total_paid_lessons
    # =========================================================

    total_lessons_map = defaultdict(int)

    for (_date, instructor_id), data in report_map.items():
        total_lessons_map[instructor_id] += data["total_lessons"]

    total_paid_lessons = []

    for instructor in instructors:

        total_paid_lessons.append(
            {
                "instructor_id": instructor.id,
                "total_lessons": total_lessons_map[instructor.id],
            }
        )

    # =========================================================
    # RESULTADO FINAL
    # =========================================================

    return {
        "lessons_per_day": lessons_per_day,
        "night_hours": night_hours,
        "total_paid_lessons": total_paid_lessons,
    }
