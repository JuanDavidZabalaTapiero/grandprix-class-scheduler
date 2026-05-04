from sqlalchemy import select
from sqlalchemy.orm import selectinload, with_loader_criteria

from app.blueprints.instructors.exceptions import (
    InstructorHasVehicles,
    InstructorNotFound,
)
from app.core.crud.services.crud import CRUDServices
from app.db.models import Instructor, InstructorVehicle, Vehicle
from app.extensions import db

# =========================
# CLASE (SERVICIOS EXTRA)
# =========================


class InstructorService(CRUDServices):

    def get_all_active_instructors(self):
        return db.session.scalars(select(Instructor).where(Instructor.enabled))

    def get_available_instructors(self):
        return db.session.scalars(
            select(Instructor)
            .options(
                selectinload(Instructor.instructor_vehicles).selectinload(
                    InstructorVehicle.vehicle
                ),
                with_loader_criteria(
                    InstructorVehicle,
                    InstructorVehicle.vehicle.has(Vehicle.enabled),
                    include_aliases=True,
                ),
            )
            .where(Instructor.enabled)
            .where(
                Instructor.instructor_vehicles.any(
                    InstructorVehicle.vehicle.has(Vehicle.enabled)
                )
            )
            .order_by(Instructor.name)
        ).all()


# =========================
# INSTANCIA
# =========================

instructor_services = InstructorService(
    Instructor,
    InstructorNotFound,
    fk_fields={"instructor_vehicles": InstructorHasVehicles},
)
