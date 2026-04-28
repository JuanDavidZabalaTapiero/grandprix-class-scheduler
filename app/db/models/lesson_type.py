from app.extensions import db


class LessonType(db.Model):
    __tablename__ = "lesson_types"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    is_default = db.Column(db.Boolean, default=False)

    # RELATIONSHIPS
    lessons = db.relationship("Lesson", back_populates="lesson_type")
