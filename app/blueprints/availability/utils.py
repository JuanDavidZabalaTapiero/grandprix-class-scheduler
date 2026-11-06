from app.db.models import (
    AvailabilityBlock,
    Enrollment,
    Student,
    StudentAvailability,
)
from app.extensions import db

WEEKDAYS = [
    (0, "Lunes"),
    (1, "Martes"),
    (2, "Miércoles"),
    (3, "Jueves"),
    (4, "Viernes"),
]


def _build_grid(blocks, weekdays, students_by_block):
    rows_by_time = {}

    for block in blocks:
        key = (block.start_time, block.end_time)

        if key not in rows_by_time:
            start = block.start_time.strftime("%I:%M %p").lstrip("0").lower()
            end = block.end_time.strftime("%I:%M %p").lstrip("0").lower()

            rows_by_time[key] = {
                "time_label": f"{start} - {end}",
                "students_by_weekday": {weekday: [] for weekday, _ in weekdays},
            }

        rows_by_time[key]["students_by_weekday"][block.weekday] = students_by_block.get(
            block.id, []
        )

    return {
        "weekdays": weekdays,
        "rows": list(rows_by_time.values()),
    }


def get_availability_grids():
    blocks = (
        db.session.query(AvailabilityBlock)
        .filter(
            AvailabilityBlock.weekday.between(0, 5),
            AvailabilityBlock.enabled.is_(True),
        )
        .order_by(
            AvailabilityBlock.start_time,
            AvailabilityBlock.end_time,
            AvailabilityBlock.weekday,
        )
        .all()
    )

    block_ids = [block.id for block in blocks]
    students_by_block = {}
    seen_student_block_pairs = set()

    if block_ids:
        available_students = (
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

        for block_id, student_id, student_name in available_students:
            pair = (block_id, student_id)

            # Evita repetir al alumno en el mismo bloque si tiene
            # más de una matrícula pendiente.
            if pair in seen_student_block_pairs:
                continue

            seen_student_block_pairs.add(pair)
            students_by_block.setdefault(block_id, []).append(student_name)

    weekday_blocks = [block for block in blocks if block.weekday <= 4]
    saturday_blocks = [block for block in blocks if block.weekday == 5]

    return {
        "weekdays_grid": _build_grid(
            weekday_blocks,
            WEEKDAYS,
            students_by_block,
        ),
        "saturday_grid": _build_grid(
            saturday_blocks,
            [(5, "Sábado")],
            students_by_block,
        ),
    }
