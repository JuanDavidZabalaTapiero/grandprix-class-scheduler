from app.extensions import db


class LessonStatus(db.Model):
    __tablename__ = "lesson_statuses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    show_in_scheduling = db.Column(db.Boolean, default=False)
    is_default = db.Column(db.Boolean, default=False)

    # RELATIONSHIPS
    lessons = db.relationship("Lesson", back_populates="lesson_status")
