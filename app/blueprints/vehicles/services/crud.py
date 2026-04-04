from app.blueprints.vehicles.exceptions import (
    VehicleLicensePlateAlreadyExists,
    VehicleNotFound,
)
from app.core.crud.services.crud import CRUDServices
from app.db.models.vehicle import Vehicle

vehicle_services = CRUDServices(
    Vehicle,
    VehicleNotFound,
    unique_fields={"license_plate": VehicleLicensePlateAlreadyExists},
)
