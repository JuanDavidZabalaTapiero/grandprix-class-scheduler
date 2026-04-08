from flask import Blueprint

instructor_vehicles_bp = Blueprint(
    "instructor_vehicles", __name__, url_prefix="/instructor-vehicles"
)

from . import routes as routes  # noqa: E402
