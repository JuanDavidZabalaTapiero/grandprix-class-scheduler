from sqlalchemy import func

from app.extensions import db


class Instructor(db.Model):
    __tablename__ = "instructors"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    contract = db.Column(db.String(50), nullable=False)
    enabled = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(
        db.DateTime, server_default=func.current_timestamp(), nullable=False
    )

    # RELATIONSHIPS
    instructor_vehicles = db.relationship(
        "InstructorVehicle", back_populates="instructor"
    )
    blocked_days = db.relationship("BlockedDay", back_populates="instructor")
