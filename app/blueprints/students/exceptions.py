from app.core.exceptions import AppError


class StudentError(AppError):
    default_message = "Ocurrió un error inesperado"


# === CREATE ===
class StudentDocumentAlreadyExists(StudentError):
    default_message = "Ya existe un estudiante con este documento"
