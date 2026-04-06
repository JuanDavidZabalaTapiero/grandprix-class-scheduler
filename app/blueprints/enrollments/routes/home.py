from flask import render_template

from app.blueprints.enrollments import enrollments_bp
from app.blueprints.enrollments.services.crud import enrollment_services
from app.core.transactions import run_query


@enrollments_bp.get("/<int:enrollment_id>")
def home(enrollment_id):
    enrollment = run_query(lambda: enrollment_services.get_by_id(enrollment_id))
    return render_template("enrollments/home.html", enrollment=enrollment)
