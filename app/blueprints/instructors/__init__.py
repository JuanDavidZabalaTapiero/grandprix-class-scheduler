from flask import Blueprint

instructors_bp = Blueprint("instructors", __name__, url_prefix="/instructors")

from . import routes as routes  # noqa: E402
