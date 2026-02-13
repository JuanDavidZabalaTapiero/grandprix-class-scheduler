from app.core.exceptions import AppError


class StudentError(AppError):
    pass


# === CREATE ===
class StudentDocumentAlreadyExists(StudentError):
    default_message = "Ya existe un alumno con este número de documento"
