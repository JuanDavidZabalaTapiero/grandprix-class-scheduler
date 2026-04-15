from app.core.exceptions import AppError


class InstructorVehicleError(AppError):
    pass


# === COMMON ===
class InstructorVehicleNotFound(InstructorVehicleError):
    default_message = "No se encontró la relación entre el instructor y el vehículo"
    status_code = 404


# === CREATE / UPDATE ===
class InstructorVehicleAlreadyExists(InstructorVehicleError):
    default_message = "El instructor ya tiene asignado este vehículo"
    status_code = 409


# === DELETE ===
class InstructorVehicleHasLessons(InstructorVehicleError):
    default_message = (
        "No se puede eliminar el vehículo del instructor porque tiene clases asociadas"
    )
    status_code = 409
