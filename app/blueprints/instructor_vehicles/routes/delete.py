from app.blueprints.instructor_vehicles import instructor_vehicles_bp
from app.blueprints.instructor_vehicles.services.crud import instructor_vehicle_services
from app.core.crud.routes.delete import DeleteRoute

DeleteRoute(
    blueprint=instructor_vehicles_bp,
    services=instructor_vehicle_services,
    url_param="instructor_vehicle_id",
    success_message="Asignación de vehículo eliminada correctamente",
    redirect_endpoint="instructor_vehicles.home",
)
