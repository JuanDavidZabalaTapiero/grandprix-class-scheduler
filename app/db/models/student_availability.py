from app.extensions import db


class StudentAvailability(db.Model):
    __tablename__ = "student_availabilities"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False,
    )
    availability_block_id = db.Column(
        db.Integer,
        db.ForeignKey("availability_blocks.id"),
        nullable=False,
    )

    student = db.relationship(
        "Student",
        back_populates="availabilities",
    )
    availability_block = db.relationship(
        "AvailabilityBlock",
        back_populates="student_availabilities",
    )
