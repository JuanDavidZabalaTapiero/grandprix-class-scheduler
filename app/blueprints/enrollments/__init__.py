from flask import Blueprint

enrollments_bp = Blueprint("enrollments", __name__, url_prefix="/enrollments")

from . import routes as routes  # noqa: E402
