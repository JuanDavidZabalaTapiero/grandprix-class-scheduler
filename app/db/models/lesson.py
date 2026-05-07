from app.core.utils.time import format_date_spanish, format_time
from app.extensions import db


class Lesson(db.Model):
    __tablename__ = "lessons"

    # PK
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)

    # DATA
    lesson_number = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    is_paid = db.Column(db.Boolean, default=True, nullable=False)
    notes = db.Column(db.String(100))

    # FK
    enrollment_id = db.Column(
        db.Integer, db.ForeignKey("enrollments.id"), nullable=False
    )
    instructor_vehicle_id = db.Column(
        db.Integer, db.ForeignKey("instructor_vehicles.id"), nullable=False
    )
    lesson_type_id = db.Column(
        db.Integer, db.ForeignKey("lesson_types.id"), nullable=False
    )
    lesson_status_id = db.Column(
        db.Integer, db.ForeignKey("lesson_statuses.id"), nullable=False
    )

    # RELATIONSHIPS
    lesson_type = db.relationship("LessonType", back_populates="lessons")
    lesson_status = db.relationship("LessonStatus", back_populates="lessons")
    enrollment = db.relationship("Enrollment", back_populates="lessons")
    instructor_vehicle = db.relationship("InstructorVehicle", back_populates="lessons")

    @property
    def formatted_date(self):
        return format_date_spanish(self.date)

    @property
    def formatted_start_time(self):
        return format_time(self.start_time)
