from app.extensions import db


class AvailabilityTimeSlot(db.Model):
    __tablename__ = "availability_time_slots"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)

    availability_blocks = db.relationship(
        "AvailabilityBlock",
        back_populates="time_slot",
    )
