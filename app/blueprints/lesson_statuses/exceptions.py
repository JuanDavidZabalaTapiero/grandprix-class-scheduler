from app.core.exceptions import AppError


class LessonStatusError(AppError):
    pass


# === COMMON ===
class LessonStatusNotFound(LessonStatusError):
    default_message = "El estado de clase no existe"
    status_code = 404


# === CREATE / UPDATE ===
class LessonStatusAlreadyExists(LessonStatusError):
    default_message = "Ya existe un estado de clase con ese nombre"
    status_code = 409
