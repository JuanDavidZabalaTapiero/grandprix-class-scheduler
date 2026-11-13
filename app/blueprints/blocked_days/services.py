from datetime import date

from sqlalchemy import select

from app.db.models import BlockedDay, InstructorBlockedSlot
from app.extensions import db

from .exceptions import (
    BlockedDayNotFound,
    BlockedSlotAlreadyExists,
    BlockedSlotNotFound,
)

# ======================================================================
# BLOCKED DAYS
# ======================================================================


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


# ======================================================================
# BLOCKED TIME SLOTS
# ======================================================================


# === CREATE ===
def create_blocked_slot(block_date, instructor_id, start_time):
    existing = db.session.scalar(
        select(InstructorBlockedSlot).where(
            InstructorBlockedSlot.instructor_id == instructor_id,
            InstructorBlockedSlot.date == block_date,
            InstructorBlockedSlot.start_time == start_time,
        )
    )

    if existing:
        raise BlockedSlotAlreadyExists()

    blocked_slot = InstructorBlockedSlot(
        date=block_date,
        start_time=start_time,
        instructor_id=instructor_id,
    )
    db.session.add(blocked_slot)
    return blocked_slot


# === READ ===
def get_blocked_slot_by_id(blocked_slot_id):
    blocked_slot = db.session.get(InstructorBlockedSlot, blocked_slot_id)

    if not blocked_slot:
        raise BlockedSlotNotFound()

    return blocked_slot


def get_blocked_slots_by_date(block_date):
    return db.session.scalars(
        select(InstructorBlockedSlot)
        .where(InstructorBlockedSlot.date == block_date)
        .order_by(
            InstructorBlockedSlot.start_time,
            InstructorBlockedSlot.instructor_id,
        )
    ).all()


def get_all_future_blocked_slots():
    return db.session.scalars(
        select(InstructorBlockedSlot)
        .where(InstructorBlockedSlot.date >= date.today())
        .order_by(
            InstructorBlockedSlot.date,
            InstructorBlockedSlot.start_time,
            InstructorBlockedSlot.instructor_id,
        )
    ).all()


# === DELETE ===
def delete_blocked_slot(blocked_slot_id):
    blocked_slot = get_blocked_slot_by_id(blocked_slot_id)
    db.session.delete(blocked_slot)
