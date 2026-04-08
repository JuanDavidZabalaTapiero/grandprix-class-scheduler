from flask import render_template

from app.blueprints.instructor_vehicles import instructor_vehicles_bp
from app.blueprints.instructor_vehicles.services.crud import instructor_vehicle_services
from app.core.transactions import run_query


@instructor_vehicles_bp.get("/")
def home():
    instructor_vehicles = run_query(lambda: instructor_vehicle_services.get_all())
    return render_template(
        "instructor_vehicles/home.html", instructor_vehicles=instructor_vehicles
    )
