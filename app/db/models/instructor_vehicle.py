from sqlalchemy import func

from app.extensions import db


class InstructorVehicle(db.Model):
    __tablename__ = "instructor_vehicles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    instructor_id = db.Column(
        db.Integer, db.ForeignKey("instructors.id"), nullable=False
    )
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.id"), nullable=False)
    created_at = db.Column(
        db.DateTime, server_default=func.current_timestamp(), nullable=False
    )

    # RELATIONSHIPS
    instructor = db.relationship("Instructor", back_populates="instructor_vehicles")
    vehicle = db.relationship("Vehicle", back_populates="instructor_vehicles")
