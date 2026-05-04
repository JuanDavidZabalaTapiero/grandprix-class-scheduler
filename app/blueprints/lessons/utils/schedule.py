from collections import defaultdict
from datetime import datetime, timedelta

from sqlalchemy.orm import joinedload

from app.core.constants import (
    EXAM_EXTRA,
    EXAM_TYPE_ID,
    LESSON_DURATION,
    MEETING_POINTS,
    PENDING_STATUS_ID,
)
from app.core.utils.time import format_date_spanish, format_time
from app.db.models import Enrollment, InstructorVehicle, Lesson


def build_schedule(enrollment_id=None, student_id=None):
    """
    Genera el cronograma agrupado por fechas y bloques consecutivos de instructor.
    """

    # -------------------------
    # 1. QUERY BASE OPTIMIZADA
    # -------------------------
    query = (
        Lesson.query.join(Lesson.instructor_vehicle)
        .join(InstructorVehicle.vehicle)
        .join(InstructorVehicle.instructor)
        .join(Lesson.enrollment)
        .options(
            joinedload(Lesson.instructor_vehicle).joinedload(InstructorVehicle.vehicle),
            joinedload(Lesson.instructor_vehicle).joinedload(
                InstructorVehicle.instructor
            ),
        )
        .filter(Lesson.lesson_status_id == PENDING_STATUS_ID)
    )

    if enrollment_id:
        query = query.filter(Lesson.enrollment_id == enrollment_id)

    if student_id:
        query = query.filter(Enrollment.student_id == student_id)

    lessons = query.all()

    if not lessons:
        return []

    total_lessons = len(lessons)

    # -------------------------
    # 2. ORDENAR (CLAVE)
    # -------------------------
    lessons.sort(
        key=lambda lesson: (
            lesson.date,
            lesson.instructor_vehicle.instructor_id,
            lesson.start_time,
        )
    )

    # -------------------------
    # 3. AGRUPAR POR FECHA
    # -------------------------
    lessons_by_date = defaultdict(list)
    for lesson in lessons:
        lessons_by_date[lesson.date].append(lesson)

    result = []

    # -------------------------
    # 4. PROCESAR CADA FECHA
    # -------------------------
    for date, day_lessons in sorted(lessons_by_date.items()):

        blocks = []
        current_block = None

        for lesson in day_lessons:
            instructor_id = lesson.instructor_vehicle.instructor_id
            vehicle = lesson.instructor_vehicle.vehicle

            lesson_datetime = datetime.combine(lesson.date, lesson.start_time)

            if current_block is None:
                # Crear primer bloque
                current_block = {
                    "instructor_id": instructor_id,
                    "start_time": lesson.start_time,
                    "lessons": [lesson],
                    "vehicles": {vehicle.id: vehicle.type},
                    "has_exam": lesson.lesson_type_id == EXAM_TYPE_ID,
                }
                continue

            # -------------------------
            # VALIDAR SI CONTINÚA BLOQUE
            # -------------------------
            last_lesson = current_block["lessons"][-1]
            last_datetime = datetime.combine(last_lesson.date, last_lesson.start_time)

            delta = lesson_datetime - last_datetime

            is_same_instructor = instructor_id == current_block["instructor_id"]
            is_consecutive = delta == timedelta(hours=1)

            if is_same_instructor and is_consecutive:
                # Continuar bloque
                current_block["lessons"].append(lesson)
                current_block["vehicles"][vehicle.id] = vehicle.type

                if lesson.lesson_type_id == EXAM_TYPE_ID:
                    current_block["has_exam"] = True
            else:
                # Cerrar bloque actual
                blocks.append(build_block(current_block))

                # Crear nuevo bloque
                current_block = {
                    "instructor_id": instructor_id,
                    "start_time": lesson.start_time,
                    "lessons": [lesson],
                    "vehicles": {vehicle.id: vehicle.type},
                    "has_exam": lesson.lesson_type_id == EXAM_TYPE_ID,
                }

        # Cerrar último bloque
        if current_block:
            blocks.append(build_block(current_block))

        result.append(
            {
                "date": format_date_spanish(date),
                "blocks": blocks,
                "total_blocks": len(blocks),
            }
        )

    return result, total_lessons


# -------------------------
# HELPER PARA CONSTRUIR BLOQUE FINAL
# -------------------------


def build_block(block):
    total_lessons = len(block["lessons"])

    # -------------------------
    # MEETING POINT
    # -------------------------
    has_first_lesson = any(lesson.lesson_number == 1 for lesson in block["lessons"])

    meeting_point = MEETING_POINTS[0] if has_first_lesson else MEETING_POINTS[1]

    # -------------------------
    # DURACIÓN
    # -------------------------
    total_minutes = total_lessons * LESSON_DURATION
    if block["has_exam"]:
        total_minutes += EXAM_EXTRA

    start_datetime = datetime.combine(block["lessons"][0].date, block["start_time"])

    end_datetime = start_datetime + timedelta(minutes=total_minutes)

    return {
        "instructor_id": block["instructor_id"],
        "start_time": format_time(block["start_time"]),
        "end_time": format_time(end_datetime.time()),
        "vehicles": [
            {"id": vid, "type": vtype} for vid, vtype in block["vehicles"].items()
        ],
        "total_lessons": total_lessons,
        "has_exam": block["has_exam"],
        "meeting_point": meeting_point,
    }
