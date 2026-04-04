from app.core.exceptions import AppError


class VehicleError(AppError):
    pass


# === COMMON ===
class VehicleNotFound(VehicleError):
    default_message = "El vehículo no existe"
    status_code = 404


# === CREATE / UPDATE ===
class VehicleLicensePlateAlreadyExists(VehicleError):
    default_message = "Ya existe un vehículo con esta placa"
    status_code = 409
