from app.core.utils.time import format_time


def build_scheduling(hours, instructors, lessons, blocked_days=None):

    # === DATOS DE EJEMPLO ===
    if blocked_days is None:
        blocked_days = []

    # === MAP LESSONS ===
    lesson_map = {
        (lesson.start_time, lesson.instructor_vehicle.instructor_id): {
            "id": lesson.id,
            "student": lesson.enrollment.student.name,
            "category": lesson.enrollment.category.name,
            "type": lesson.lesson_type.name,
            "vehicle_id": lesson.instructor_vehicle.vehicle.id,
            "vehicle_license": lesson.instructor_vehicle.vehicle.license_plate,
            "vehicle_type": lesson.instructor_vehicle.vehicle.type,
        }
        for lesson in lessons
    }

    # === MAP BLOCKED DAYS ===
    blocked_instructor_ids = {block.instructor_id for block in blocked_days}

    # === ARRAY VEHICLES ID ===
    vehicles_by_hour = {}

    for lesson in lessons:
        hour = lesson.start_time
        vehicle_id = lesson.instructor_vehicle.vehicle.id
        vehicles_by_hour.setdefault(hour, set()).add(vehicle_id)

    vehicles_by_hour = {str(hour): list(v) for hour, v in vehicles_by_hour.items()}

    # === DICT ===
    return [
        {
            "hour": str(hour),
            "hour_formatted": format_time(hour),
            "vehicles_ids": vehicles_by_hour.get(str(hour), []),
            "instructors": [
                {
                    "id": i.id,
                    "is_blocked": i.id in blocked_instructor_ids,
                    "lesson": lesson_map.get((hour, i.id)),
                }
                for i in instructors
            ],
        }
        for hour in hours
    ]
