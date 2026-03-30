from flask import render_template

from app.blueprints.instructors import instructors_bp
from app.blueprints.instructors.services.crud import instructor_services


@instructors_bp.get("/")
def home():
    instructors = instructor_services.get_all()
    return render_template("instructors/home.html", instructors=instructors)
