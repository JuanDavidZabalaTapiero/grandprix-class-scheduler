import logging
from typing import List

from sqlalchemy import or_
from sqlalchemy.exc import OperationalError, SQLAlchemyError

from app.blueprints.students.exceptions import StudentError
from app.db.exceptions import DatabaseConnectionError
from app.db.models import Student

logger = logging.getLogger(__name__)


# =========================
# SERVICE
# =========================


def search_students(term: str) -> List[Student]:
    try:
        if not term:
            return []

        students = (
            Student.query.filter(
                or_(
                    Student.document_id.ilike(f"%{term}%"),
                    Student.name.ilike(f"%{term}%"),
                )
            )
            .order_by(Student.name.asc())
            .limit(20)
            .all()
        )

        return students

    except OperationalError as e:
        logger.exception("Database connection error while searching students")
        raise DatabaseConnectionError() from e

    except SQLAlchemyError as e:
        logger.exception("Unexpected SQLAlchemyError while searching | term=%s", term)
        raise StudentError() from e
