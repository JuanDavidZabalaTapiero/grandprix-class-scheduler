from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError

from app.blueprints.students.exceptions import (
    StudentDocumentAlreadyExists,
    StudentError,
)
from app.db.exceptions import DatabaseConnectionError
from app.db.models import Student
from app.extensions import db


def create_student(data: dict) -> Student:
    try:
        # DATOS + LIMPIEZA
        document_id = data["document_id"].strip()
        name = data["name"].strip()
        phone = data["phone"].strip()

        # REGISTRAR
        student = Student(document_id=document_id, name=name, phone=phone)

        db.session.add(student)
        db.session.commit()

        return student

    except IntegrityError as e:
        db.session.rollback()
        raise StudentDocumentAlreadyExists() from e

    except OperationalError as e:
        db.session.rollback()
        raise DatabaseConnectionError() from e

    except SQLAlchemyError as e:
        db.session.rollback()
        raise StudentError() from e
