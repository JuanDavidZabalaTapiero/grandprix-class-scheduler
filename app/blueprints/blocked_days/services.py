from datetime import date

from app.db.models.blocked_days import BlockedDay
from app.extensions import db

from .exceptions import BlockedDayNotFound


# === CREATE ===
def create_blocked_day(date, instructor_id):
    new_obj = BlockedDay(date=date, instructor_id=instructor_id)
    db.session.add(new_obj)
    return new_obj


# === READ ===
def get_blocked_day_by_id(id):
    obj = db.session.get(BlockedDay, id)

    if not obj:
        raise BlockedDayNotFound

    return obj


def get_blocked_days_by_date(date):
    return db.session.scalars(
        db.select(BlockedDay).where(BlockedDay.date == date)
    ).all()


def get_all_future_blocked_days():
    return db.session.scalars(
        db.select(BlockedDay).where(BlockedDay.date >= date.today())
    ).all()


# === DELETE ===
def delete_blocked_day(id):
    obj = get_blocked_day_by_id(id)
    db.session.delete(obj)
