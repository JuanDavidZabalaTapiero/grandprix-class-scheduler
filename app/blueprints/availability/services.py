from sqlalchemy import delete, select

from app.db.models import AvailabilityBlock, StudentAvailability
from app.extensions import db


def replace_student_availabilities(student_id, selected_block_ids):
    enabled_block_ids = set(
        db.session.scalars(
            select(AvailabilityBlock.id).where(AvailabilityBlock.enabled.is_(True))
        ).all()
    )

    # Limita los cambios a bloques activos que aparecen en las matrices.
    selected_block_ids = set(selected_block_ids) & enabled_block_ids

    if enabled_block_ids:
        db.session.execute(
            delete(StudentAvailability).where(
                StudentAvailability.student_id == student_id,
                StudentAvailability.availability_block_id.in_(enabled_block_ids),
            )
        )

    db.session.add_all(
        StudentAvailability(
            student_id=student_id,
            availability_block_id=block_id,
        )
        for block_id in selected_block_ids
    )
