from sqlalchemy import func

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
