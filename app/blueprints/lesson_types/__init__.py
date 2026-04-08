from flask import Blueprint

lesson_types_bp = Blueprint("lesson_types", __name__, url_prefix="/lesson-types")

from . import routes as routes  # noqa: E402
