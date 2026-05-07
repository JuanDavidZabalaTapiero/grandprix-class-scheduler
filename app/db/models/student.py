from operator import attrgetter

from sqlalchemy import func

from app.core.constants import ABSENCE_PRICE, ABSENCE_STATUS_ID
from app.extensions import db


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    document_id = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    created_at = db.Column(
        db.DateTime, server_default=func.current_timestamp(), nullable=False
    )

    # RELATIONSHIPS
    enrollments = db.relationship("Enrollment", back_populates="student")

    # ABSENCE
    @property
    def lessons_with_absence(self):
        lessons = [
            lesson
            for enrollment in self.enrollments
            for lesson in enrollment.lessons
            if lesson.lesson_status_id == ABSENCE_STATUS_ID
        ]

        return sorted(lessons, key=attrgetter("date", "start_time"))

    @property
    def absence_count(self):
        return len(self.lessons_with_absence)

    @property
    def absence_total(self):
        return self.absence_count * ABSENCE_PRICE
