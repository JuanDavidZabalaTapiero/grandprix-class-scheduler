from app.blueprints.vehicles import vehicles_bp
from app.blueprints.vehicles.forms.vehicle_form import VehicleForm
from app.blueprints.vehicles.services.crud import vehicle_services
from app.core.crud.routes.crud import CRUDRoutes
from app.schemas.vehicle import VehicleSchema

CRUDRoutes(
    blueprint=vehicles_bp,
    services=vehicle_services,
    schema=VehicleSchema,
    form_model=VehicleForm,
    list=dict(
        template="vehicles/home.html",
        context_name="vehicles",
    ),
    create=dict(
        template="vehicles/form.html",
        success_message="Vehículo registrado correctamente",
        redirect_endpoint="vehicles.home",
    ),
    update=dict(
        template="vehicles/form.html",
        url_param="vehicle_id",
        success_message="Vehículo actualizado correctamente",
        redirect_endpoint="vehicles.home",
    ),
    delete=dict(
        url_param="vehicle_id",
        success_message="Vehículo eliminado correctamente",
        redirect_endpoint="vehicles.home",
    ),
)
