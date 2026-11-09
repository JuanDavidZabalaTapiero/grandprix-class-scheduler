from app.db.models import (
    AvailabilityBlock,
    AvailabilityTimeSlot,
)
from app.extensions import db

WEEKDAY_COLUMNS = [
    (0, "Lunes", "monday"),
    (1, "Martes", "tuesday"),
    (2, "Miércoles", "wednesday"),
    (3, "Jueves", "thursday"),
    (4, "Viernes", "friday"),
]

# ======================================================================
# REGISTRO DE HORARIOS
# ======================================================================


def _format_time_slot(time_slot):
    start = time_slot.start_time.strftime("%I:%M %p").lstrip("0").lower()
    end = time_slot.end_time.strftime("%I:%M %p").lstrip("0").lower()
    return f"{start} - {end}"


def get_weekday_availability_matrix():
    blocks = (
        db.session.query(AvailabilityBlock, AvailabilityTimeSlot)
        .join(
            AvailabilityTimeSlot,
            AvailabilityTimeSlot.id == AvailabilityBlock.time_slot_id,
        )
        .filter(
            AvailabilityBlock.weekday.between(0, 4),
            AvailabilityBlock.enabled.is_(True),
        )
        .order_by(
            AvailabilityTimeSlot.start_time,
            AvailabilityTimeSlot.end_time,
            AvailabilityBlock.weekday,
        )
        .all()
    )

    rows_by_time_slot = {}

    for block, time_slot in blocks:
        key = (time_slot.start_time, time_slot.end_time)

        if key not in rows_by_time_slot:
            rows_by_time_slot[key] = {
                "time_slot": _format_time_slot(time_slot),
                **{column_key: None for _, _, column_key in WEEKDAY_COLUMNS},
            }

        column_key = next(
            column_key
            for weekday, _, column_key in WEEKDAY_COLUMNS
            if weekday == block.weekday
        )
        rows_by_time_slot[key][column_key] = block.id

    return {
        "weekdays": [name for _, name, _ in WEEKDAY_COLUMNS],
        "rows": list(rows_by_time_slot.values()),
    }


def get_saturday_availability_matrix():
    blocks = (
        db.session.query(AvailabilityBlock, AvailabilityTimeSlot)
        .join(
            AvailabilityTimeSlot,
            AvailabilityTimeSlot.id == AvailabilityBlock.time_slot_id,
        )
        .filter(
            AvailabilityBlock.weekday == 5,
            AvailabilityBlock.enabled.is_(True),
        )
        .order_by(
            AvailabilityTimeSlot.start_time,
            AvailabilityTimeSlot.end_time,
        )
        .all()
    )

    return {
        "weekdays": ["Sábado"],
        "rows": [
            {
                "time_slot": _format_time_slot(time_slot),
                "saturday": block.id,
            }
            for block, time_slot in blocks
        ],
    }
