from app.extensions import db


class BlockedDay(db.Model):
    __tablename__ = "blocked_days"

    # UNIQUE: DATE & INSTRUCTOR_ID
    __table_args__ = (
        db.UniqueConstraint(
            "date", "instructor_id", name="ux_blocked_days_date_instructor"
        ),
    )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    date = db.Column(db.Date, nullable=False)
    instructor_id = db.Column(
        db.Integer, db.ForeignKey("instructors.id"), nullable=False
    )

    instructor = db.relationship("Instructor", back_populates="blocked_days")
