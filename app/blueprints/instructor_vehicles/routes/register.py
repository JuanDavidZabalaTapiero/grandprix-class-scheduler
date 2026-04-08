from app.blueprints.instructor_vehicles import instructor_vehicles_bp
from app.blueprints.instructor_vehicles.forms.instructor_vehicle_form import (
    InstructorVehicleForm,
)
from app.blueprints.instructor_vehicles.services.crud import instructor_vehicle_services
from app.blueprints.instructors.services.crud import instructor_services
from app.blueprints.vehicles.services.crud import vehicle_services
from app.core.crud.routes.create import CreateRoute
from app.schemas.instructor_vehicle import InstructorVehicleSchema

# =========================
# CLASE (CONFIG EXTRA)
# =========================


class InstructorVehicleCreateRoute(CreateRoute):

    def setup_form(self, form):

        # INSTRUCTORS
        instructors = instructor_services.get_all()
        if not instructors:
            form.instructor_id.choices = [(0, "No hay instructores registrados")]
            form.instructor_id.render_kw = {"disabled": True}
        else:
            form.instructor_id.choices = [(i.id, i.name) for i in instructors]

        # VEHICLES
        vehicles = vehicle_services.get_all()
        if not vehicles:
            form.vehicle_id.choices = [(0, "No hay vehículos registrados")]
            form.vehicle_id.render_kw = {"disabled": True}
        else:
            form.vehicle_id.choices = [
                (v.id, f"{v.license_plate} | {v.brand}") for v in vehicles
            ]


# =========================
# CREAR RUTA
# =========================


InstructorVehicleCreateRoute(
    blueprint=instructor_vehicles_bp,
    form=InstructorVehicleForm,
    template="instructor_vehicles/register.html",
    services=instructor_vehicle_services,
    schema=InstructorVehicleSchema,
    success_message="Instructor asignado al vehículo correctamente",
    redirect_endpoint="instructors.home",
)
