from sqlalchemy import select

from app.blueprints.instructor_vehicles.exceptions import (
    InstructorVehicleAlreadyExists,
    InstructorVehicleHasLessons,
    InstructorVehicleNotFound,
)
from app.core.crud.services.crud import CRUDServices
from app.db.models.instructor_vehicle import InstructorVehicle
from app.extensions import db

# =========================
# CLASE (SERVICIOS EXTRA)
# =========================


class InstructorVehicleService(CRUDServices):

    def exists(self, instructor_id, vehicle_id):
        return db.session.scalar(
            select(InstructorVehicle).where(
                InstructorVehicle.instructor_id == instructor_id,
                InstructorVehicle.vehicle_id == vehicle_id,
            )
        )

    def create(self, data: dict):

        # === VALIDACIÓN ===

        # DUPLICADO
        existing = self.exists(data["instructor_id"], data["vehicle_id"])
        if existing:
            raise InstructorVehicleAlreadyExists()

        # === REGISTRO ===
        return super().create(
            {"instructor_id": data["instructor_id"], "vehicle_id": data["vehicle_id"]}
        )


# =========================
# INSTANCIA
# =========================

instructor_vehicle_services = InstructorVehicleService(
    InstructorVehicle,
    InstructorVehicleNotFound,
    fk_fields={"lessons": InstructorVehicleHasLessons},
)
