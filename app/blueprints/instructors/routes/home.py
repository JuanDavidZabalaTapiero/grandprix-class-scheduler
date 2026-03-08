from flask import render_template

from app.blueprints.instructors import instructors_bp  # BLUEPRINT
from app.blueprints.instructors.services.get_instructor import (
    get_all_instructors,
)  # SERVICIO


@instructors_bp.get("/")
def home():
    instructors = get_all_instructors()
    return render_template("instructors/home.html", instructors=instructors)
