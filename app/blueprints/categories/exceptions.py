from app.core.exceptions import AppError


class CategoryError(AppError):
    pass


# === COMMON ===
class CategoryNotFound(CategoryError):
    default_message = "La categoría no existe"
    status_code = 404


# === CREATE / UPDATE ===
class CategoryAlreadyExists(CategoryError):
    default_message = "Ya existe una categoría con ese nombre"
    status_code = 409


# === DELETE ===
class CategoryHasEnrollments(AppError):
    default_message = (
        "No se puede eliminar la categoría porque tiene matrículas asociadas"
    )
    status_code = 409
