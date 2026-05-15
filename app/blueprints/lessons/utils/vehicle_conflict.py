from sqlalchemy import select

from app.db.models import InstructorVehicle, Lesson
from app.extensions import db


def is_vehicle_busy(vehicle_id, lesson):

    stmt = (
        select(Lesson)
        .join(InstructorVehicle)
        .where(
            InstructorVehicle.vehicle_id == vehicle_id,
            Lesson.date == lesson.date,
            Lesson.start_time == lesson.start_time,
            Lesson.id != lesson.id,
        )
    )

    conflicting_lesson = db.session.scalar(stmt)

    return conflicting_lesson is not None
