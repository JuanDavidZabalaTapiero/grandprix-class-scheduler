from sqlalchemy import select

from app.blueprints.lessons.exceptions import LessonNotFound
from app.core.crud.services.crud import CRUDServices
from app.db.models import InstructorVehicle, Lesson, LessonStatus, LessonType
from app.extensions import db

# =========================
# CLASE (SERVICIOS EXTRA)
# =========================


class LessonService(CRUDServices):

    # === READ ===
    def get_schedule(self, date, instructors):
        instructors_ids = [i.id for i in instructors]

        return db.session.scalars(
            select(Lesson)
            .join(InstructorVehicle)
            .join(LessonStatus)
            .where(Lesson.date == date)
            .where(InstructorVehicle.instructor_id.in_(instructors_ids))
            .where(LessonStatus.show_in_schedule)
        ).all()

    def get_default_type(self):
        return db.session.scalar(select(LessonType).where(LessonType.is_default))

    def get_default_status(self):
        return db.session.scalar(select(LessonStatus).where(LessonStatus.is_default))

    def get_lessons(self, enrollment_id):
        return db.session.scalars(
            select(Lesson)
            .where(Lesson.enrollment_id == enrollment_id)
            .order_by(Lesson.date.asc(), Lesson.start_time.asc())
        ).all()

    # === CREATE ===
    def bulk_create(self, data):

        # DATA
        enrollment_id = data["enrollment_id"]
        lessons = data["lessons"]
        default_type = self.get_default_type()
        default_status = self.get_default_status()

        # REGISTRO
        for lesson in lessons:
            lesson_data = {
                "lesson_number": 1,
                "date": lesson["date"],
                "start_time": lesson["hour"],
                "enrollment_id": enrollment_id,
                "instructor_vehicle_id": lesson["instructor_vehicle_id"],
                "lesson_type_id": default_type.id,
                "lesson_status_id": default_status.id,
            }

            super().create(lesson_data)

    # === UPDATE ===
    def organize_lesson_number(self, enrollment_id):

        # QUERY
        lessons = db.session.scalars(
            select(Lesson)
            .join(LessonStatus)
            .where(
                Lesson.enrollment_id == enrollment_id,
                LessonStatus.show_in_schedule,
            )
            .order_by(Lesson.date.asc(), Lesson.start_time.asc())
        ).all()

        # ASIGNAR NÚMEROS
        for idx, lesson in enumerate(lessons, start=1):
            lesson.lesson_number = idx

        return lessons

    # === DELETE ===
    def bulk_delete(self, lessons):
        Lesson.query.filter(Lesson.id.in_(lessons)).delete(synchronize_session=False)


# =========================
# INSTANCIA
# =========================

lesson_services = LessonService(Lesson, LessonNotFound)
