from dataclasses import dataclass

from app.core.crud.services import create_model
from app.db.models import Instructor

# =========================
# INPUT CONTRACT
# =========================


@dataclass
class CreateInstructorInput:
    name: str
    phone: str
    contract: str
    enabled: bool


# =========================
# SERVICE
# =========================


def create_instructor(data: CreateInstructorInput) -> Instructor:
    instructor = create_model(
        Instructor,
        {
            "name": data.name,
            "phone": data.phone,
            "contract": data.contract,
            "enabled": data.enabled,
        },
    )
    return instructor
