from app.forms.fields import select_field


def instructor_id_field():
    return select_field("Instructor")


def vehicle_id_field():
    return select_field("Vehículo")
