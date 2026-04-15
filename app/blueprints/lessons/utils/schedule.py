def build_schedule(hours, instructors, lessons):

    # MAP
    lesson_map = {
        (lesson.start_time, lesson.instructor_vehicle.instructor_id): {
            "id": lesson.id,
            "student": lesson.enrollment.student.name,
            "category": lesson.enrollment.category.name,
            "vehicle_id": lesson.instructor_vehicle.vehicle.id,
            "vehicle_license": lesson.instructor_vehicle.vehicle.license_plate,
            "vehicle_type": lesson.instructor_vehicle.vehicle.type,
        }
        for lesson in lessons
    }

    # ARRAY VEHICLES ID
    vehicles_by_hour = {}

    for lesson in lessons:
        hour = lesson.start_time
        vehicle_id = lesson.instructor_vehicle.vehicle.id
        vehicles_by_hour.setdefault(hour, set()).add(vehicle_id)

    vehicles_by_hour = {str(hour): list(v) for hour, v in vehicles_by_hour.items()}

    # DICT
    return [
        {
            "hour": str(hour),
            "vehicles_ids": vehicles_by_hour.get(str(hour), []),
            "instructors": [
                {"id": i.id, "lesson": lesson_map.get((hour, i.id))}
                for i in instructors
            ],
        }
        for hour in hours
    ]
