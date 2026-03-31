from app.core.exceptions import AppError


class CategoryError(AppError):
    pass


# === COMMON ===
class CategoryNotFound(CategoryError):
    default_message = "La categoría no existe"
    status_code = 404
