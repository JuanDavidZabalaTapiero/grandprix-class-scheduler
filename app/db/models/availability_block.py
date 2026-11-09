from app.extensions import db


class AvailabilityBlock(db.Model):
    __tablename__ = "availability_blocks"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    weekday = db.Column(db.SmallInteger, nullable=False)
    time_slot_id = db.Column(
        db.Integer,
        db.ForeignKey("availability_time_slots.id"),
        nullable=False,
    )
    enabled = db.Column(
        db.Boolean,
        default=True,
        server_default=db.true(),
        nullable=False,
    )

    time_slot = db.relationship(
        "AvailabilityTimeSlot",
        back_populates="availability_blocks",
    )
    student_availabilities = db.relationship(
        "StudentAvailability",
        back_populates="availability_block",
    )
