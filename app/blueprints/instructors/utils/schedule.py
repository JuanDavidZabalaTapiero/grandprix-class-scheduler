from datetime import datetime, timedelta

from sqlalchemy import select

from app.core.constants import EXAM_EXTRA, EXAM_TYPE_ID, LESSON_DURATION
from app.core.utils.time import format_time
from app.db.models import InstructorVehicle, Lesson, LessonStatus
from app.extensions import db


def build_instructor_schedule(instructor_id, date):
    """
    Construye el horario de un instructor agrupando lecciones en bloques.

    Un bloque se forma cuando:
    - Mismo estudiante
    - Misma categoría
    - Clases consecutivas con diferencia EXACTA de 1 hora
    """

    # -------------------------
    # 1. LESSONS (QUERY)
    # -------------------------
    lessons = db.session.scalars(
        select(Lesson)
        .join(InstructorVehicle)
        .join(LessonStatus)
        .where(Lesson.date == date)
        .where(InstructorVehicle.instructor_id == instructor_id)
        .where(LessonStatus.show_in_scheduling)
    ).all()

    if not lessons:
        return []

    # -------------------------
    # 2. PRELOAD RELATIONS
    # -------------------------
    def enrich(lesson):
        enrollment = lesson.enrollment
        student = enrollment.student
        category = enrollment.category
        instructor_vehicle = lesson.instructor_vehicle
        vehicle = instructor_vehicle.vehicle

        return {
            "lesson": lesson,
            "start_time": lesson.start_time,
            "lesson_number": lesson.lesson_number,
            "lesson_type_id": lesson.lesson_type_id,
            "student_id": student.id,
            "student_name": student.name,
            "student_phone": student.phone,
            "category_id": category.id,
            "category_name": category.name,
            "vehicle_id": vehicle.id,
            "license_plate": vehicle.license_plate,
        }

    enriched_lessons = [enrich(lesson) for lesson in lessons]

    # -------------------------
    # 3. SORT LESSONS
    # -------------------------
    enriched_lessons.sort(key=lambda x: x["start_time"])

    # -------------------------
    # 4. BUILD BLOCKS
    # -------------------------
    blocks = []
    current_block = None

    for item in enriched_lessons:
        if current_block is None:
            current_block = _create_block(item)
            continue

        if _belongs_to_block(current_block, item):
            _add_to_block(current_block, item)
        else:
            blocks.append(_finalize_block(current_block))
            current_block = _create_block(item)

    # último bloque
    if current_block:
        blocks.append(_finalize_block(current_block))

    # -------------------------
    # 5. SORT FINAL (por start_time)
    # -------------------------
    blocks.sort(key=lambda x: x["start_time"])

    return blocks


# =========================================================
# HELPERS
# =========================================================


def _create_block(item):
    """Inicializa un nuevo bloque."""
    return {
        "category_id": item["category_id"],
        "category_name": item["category_name"],
        "student_id": item["student_id"],
        "student_name": item["student_name"],
        "student_phone": item["student_phone"],
        "start_time": item["start_time"],
        "last_time": item["start_time"],
        "total_lessons": 1,
        "lowest_lesson_number": item["lesson_number"],
        "vehicles": {
            item["vehicle_id"]: {
                "vehicle_id": item["vehicle_id"],
                "license_plate": item["license_plate"],
            }
        },
        "has_exam": item["lesson_type_id"] == EXAM_TYPE_ID,
    }


def _belongs_to_block(block, item):
    """
    Determina si una lección pertenece al bloque actual.
    """

    # mismo estudiante y categoría
    if block["student_id"] != item["student_id"]:
        return False

    if block["category_id"] != item["category_id"]:
        return False

    # diferencia EXACTA de 1 hora
    expected_time = (
        datetime.combine(datetime.today(), block["last_time"]) + timedelta(hours=1)
    ).time()

    return item["start_time"] == expected_time


def _add_to_block(block, item):
    """Agrega una lección al bloque existente."""

    block["last_time"] = item["start_time"]
    block["total_lessons"] += 1

    block["lowest_lesson_number"] = min(
        block["lowest_lesson_number"], item["lesson_number"]
    )

    # vehículos sin duplicados
    if item["vehicle_id"] not in block["vehicles"]:
        block["vehicles"][item["vehicle_id"]] = {
            "vehicle_id": item["vehicle_id"],
            "license_plate": item["license_plate"],
        }

    # examen
    if item["lesson_type_id"] == EXAM_TYPE_ID:
        block["has_exam"] = True


def _finalize_block(block):
    """Calcula end_time y transforma estructura final."""

    total_minutes = block["total_lessons"] * LESSON_DURATION

    if block["has_exam"]:
        total_minutes += EXAM_EXTRA

    start_dt = datetime.combine(datetime.today(), block["start_time"])
    end_dt = start_dt + timedelta(minutes=total_minutes)

    return {
        "category_id": block["category_id"],
        "category_name": block["category_name"],
        "student_id": block["student_id"],
        "student_name": block["student_name"],
        "student_phone": block["student_phone"],
        "start_time": block["start_time"],
        "formatted_start_time": format_time(block["start_time"]),
        "end_time": end_dt.time(),
        "formatted_end_time": format_time(end_dt.time()),
        "total_lessons": block["total_lessons"],
        "lowest_lesson_number": block["lowest_lesson_number"],
        "vehicles": list(block["vehicles"].values()),
        "has_exam": block["has_exam"],
    }
