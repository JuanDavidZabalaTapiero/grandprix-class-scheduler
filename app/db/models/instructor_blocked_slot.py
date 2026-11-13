from app.extensions import db


class InstructorBlockedSlot(db.Model):
    __tablename__ = "instructor_blocked_slots"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    instructor_id = db.Column(
        db.Integer,
        db.ForeignKey("instructors.id"),
        nullable=False,
    )
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)

    instructor = db.relationship(
        "Instructor",
        back_populates="blocked_slots",
    )
