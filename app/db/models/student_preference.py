from app.extensions import db


class StudentPreference(db.Model):
    __tablename__ = "student_preferences"

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        primary_key=True,
    )
    wants_automatic = db.Column(
        db.Boolean,
        default=False,
        server_default=db.false(),
        nullable=False,
    )

    student = db.relationship("Student", back_populates="preferences")
