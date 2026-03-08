import logging
from typing import List

from sqlalchemy import or_, select

from app.db.decorators import handle_db_exceptions
from app.db.models import Student
from app.extensions import db

logger = logging.getLogger(__name__)


# =========================
# SERVICE
# =========================


@handle_db_exceptions
def search_students(term: str) -> List[Student]:
    students = db.session.scalars(
        select(Student)
        .where(
            or_(
                Student.document_id.ilike(f"%{term}%"),
                Student.name.ilike(f"%{term}%"),
            )
        )
        .order_by(Student.name.asc())
        .limit(20)
    ).all()

    return students
