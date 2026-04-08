from flask import Blueprint

lesson_statuses_bp = Blueprint(
    "lesson_statuses", __name__, url_prefix="/lesson-statuses"
)

from . import routes as routes  # noqa: E402
