from app.core.utils.time import format_time


def build_scheduling(
    hours,
    instructors,
    lessons,
    blocked_days=None,
    blocked_slots=None,
):
    if blocked_days is None:
        blocked_days = []

    if blocked_slots is None:
        blocked_slots = []

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

    blocked_instructor_ids = {blocked_day.instructor_id for blocked_day in blocked_days}

    blocked_slot_keys = {
        (blocked_slot.instructor_id, blocked_slot.start_time)
        for blocked_slot in blocked_slots
    }

    vehicles_by_hour = {}

    for lesson in lessons:
        vehicle_id = lesson.instructor_vehicle.vehicle.id
        vehicles_by_hour.setdefault(lesson.start_time, set()).add(vehicle_id)

    vehicles_by_hour = {
        str(hour): list(vehicle_ids) for hour, vehicle_ids in vehicles_by_hour.items()
    }

    return [
        {
            "hour": str(hour),
            "hour_formatted": format_time(hour),
            "vehicles_ids": vehicles_by_hour.get(str(hour), []),
            "instructors": [
                {
                    "id": instructor.id,
                    "is_blocked": instructor.id in blocked_instructor_ids,
                    "is_time_blocked": (
                        instructor.id,
                        hour,
                    )
                    in blocked_slot_keys,
                    "lesson": lesson_map.get((hour, instructor.id)),
                }
                for instructor in instructors
            ],
        }
        for hour in hours
    ]
