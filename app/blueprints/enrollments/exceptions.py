from app.core.exceptions import AppError


class EnrollmentError(AppError):
    pass


# === COMMON ===
class EnrollmentNotFound(EnrollmentError):
    default_message = "La matrícula no existe"
    status_code = 404


# === CREATE / UPDATE ===
class EnrollmentAlreadyExists(EnrollmentError):
    default_message = "El alumno ya está matriculado en esta categoría"
    status_code = 409
