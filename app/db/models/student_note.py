from sqlalchemy import func

from app.extensions import db


class StudentNote(db.Model):
    __tablename__ = "student_notes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False,
    )
    note = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime,
        server_default=func.current_timestamp(),
        nullable=False,
    )
