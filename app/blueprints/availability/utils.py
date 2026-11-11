from app.db.models import (
    AvailabilityBlock,
    AvailabilityTimeSlot,
    Enrollment,
    Student,
    StudentAvailability,
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


# ======================================================================
# HORARIOS DE ALUMNOS PENDIENTES
# ======================================================================


def _build_pending_students_matrix(weekday_columns):
    weekdays = [weekday for weekday, _, _ in weekday_columns]

    blocks = (
        db.session.query(AvailabilityBlock, AvailabilityTimeSlot)
        .join(
            AvailabilityTimeSlot,
            AvailabilityTimeSlot.id == AvailabilityBlock.time_slot_id,
        )
        .filter(
            AvailabilityBlock.weekday.in_(weekdays),
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
    students_by_block = {}

    for block, time_slot in blocks:
        time_key = (time_slot.start_time, time_slot.end_time)

        if time_key not in rows_by_time_slot:
            rows_by_time_slot[time_key] = {
                "time_slot": _format_time_slot(time_slot),
                **{
                    column_key: {"students": []} for _, _, column_key in weekday_columns
                },
            }

        column_key = next(
            column_key
            for weekday, _, column_key in weekday_columns
            if weekday == block.weekday
        )

        cell_students = rows_by_time_slot[time_key][column_key]["students"]
        students_by_block[block.id] = (time_key, column_key, cell_students)

    block_ids = list(students_by_block)

    if block_ids:
        assignments = (
            db.session.query(
                StudentAvailability.availability_block_id,
                Student.id,
                Student.name,
            )
            .join(
                Student,
                Student.id == StudentAvailability.student_id,
            )
            .join(
                Enrollment,
                Enrollment.student_id == Student.id,
            )
            .filter(
                StudentAvailability.availability_block_id.in_(block_ids),
                Enrollment.schedule_completed.is_(False),
            )
            .order_by(Student.created_at, Student.id)
            .all()
        )

        seen_students = set()

        for block_id, student_id, student_name in assignments:
            time_key, column_key, cell_students = students_by_block[block_id]
            student_cell_key = (time_key, column_key, student_id)

            # Si tiene varias matrículas pendientes, aparece una sola vez
            # en la misma celda.
            if student_cell_key in seen_students:
                continue

            seen_students.add(student_cell_key)
            cell_students.append({"student_name": student_name})

    return {
        "weekdays": [name for _, name, _ in weekday_columns],
        "rows": list(rows_by_time_slot.values()),
    }


def get_weekday_pending_students_matrix():
    return _build_pending_students_matrix(WEEKDAY_COLUMNS)


def get_saturday_pending_students_matrix():
    saturday_column = [(5, "Sábado", "saturday")]
    return _build_pending_students_matrix(saturday_column)


# ======================================================================
# HORARIOS DE UN ALUMNO
# ======================================================================


def _build_student_availability_matrix(student_id, weekday_columns):
    weekdays = [weekday for weekday, _, _ in weekday_columns]

    blocks = (
        db.session.query(AvailabilityBlock, AvailabilityTimeSlot)
        .join(
            AvailabilityTimeSlot,
            AvailabilityTimeSlot.id == AvailabilityBlock.time_slot_id,
        )
        .filter(
            AvailabilityBlock.weekday.in_(weekdays),
            AvailabilityBlock.enabled.is_(True),
        )
        .order_by(
            AvailabilityTimeSlot.start_time,
            AvailabilityTimeSlot.end_time,
            AvailabilityBlock.weekday,
        )
        .all()
    )

    block_ids = [block.id for block, _ in blocks]

    if block_ids:
        selected_block_ids = {
            row[0]
            for row in (
                db.session.query(StudentAvailability.availability_block_id)
                .filter(
                    StudentAvailability.student_id == student_id,
                    StudentAvailability.availability_block_id.in_(block_ids),
                )
                .all()
            )
        }
    else:
        selected_block_ids = set()

    rows_by_time_slot = {}

    for block, time_slot in blocks:
        time_key = (time_slot.start_time, time_slot.end_time)

        if time_key not in rows_by_time_slot:
            rows_by_time_slot[time_key] = {
                "time_slot": _format_time_slot(time_slot),
                **{column_key: None for _, _, column_key in weekday_columns},
            }

        column_key = next(
            column_key
            for weekday, _, column_key in weekday_columns
            if weekday == block.weekday
        )

        rows_by_time_slot[time_key][column_key] = {
            "block_id": block.id,
            "available": block.id in selected_block_ids,
        }

    return {
        "weekdays": [name for _, name, _ in weekday_columns],
        "rows": list(rows_by_time_slot.values()),
    }


def get_student_weekday_availability_matrix(student_id):
    return _build_student_availability_matrix(student_id, WEEKDAY_COLUMNS)


def get_student_saturday_availability_matrix(student_id):
    saturday_column = [(5, "Sábado", "saturday")]
    return _build_student_availability_matrix(student_id, saturday_column)
