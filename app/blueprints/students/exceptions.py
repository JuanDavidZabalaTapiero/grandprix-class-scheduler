from app.core.exceptions import AppError


class StudentError(AppError):
    pass


# === COMMON ===
class StudentNotFound(StudentError):
    default_message = "El alumno no existe"
    status_code = 404


# === CREATE / UPDATE ===
class StudentDocumentAlreadyExists(StudentError):
    default_message = "Ya existe un alumno con este número de documento"
    status_code = 409


# === DELETE ===
class StudentHasEnrollments(AppError):
    default_message = "No se puede eliminar al alumno porque tiene matrículas asociadas"
    status_code = 409
