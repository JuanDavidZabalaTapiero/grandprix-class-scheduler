from app.extensions import db


class AvailabilityBlock(db.Model):
    __tablename__ = "availability_blocks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    weekday = db.Column(db.SmallInteger, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    enabled = db.Column(db.Boolean, default=True, nullable=False)
