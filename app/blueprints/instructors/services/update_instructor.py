from dataclasses import dataclass

from app.core.crud.services import update_model
from app.db.models import Instructor

# =========================
# INPUT CONTRACT
# =========================


@dataclass
class UpdateInstructorInput:
    instructor: Instructor
    name: str
    phone: str
    contract: str
    enabled: bool


# =========================
# SERVICE
# =========================


def update_instructor(data: UpdateInstructorInput) -> Instructor:
    instructor = update_model(
        data.instructor,
        {
            "name": data.name,
            "phone": data.phone,
            "contract": data.contract,
            "enabled": data.enabled,
        },
    )
    return instructor
