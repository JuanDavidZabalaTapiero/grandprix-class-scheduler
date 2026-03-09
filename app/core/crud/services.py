from sqlalchemy import select

from app.db.decorators import handle_db_exceptions
from app.extensions import db


# === CREATE ===
def create_model(model, data: dict):
    obj = model(**data)

    db.session.add(obj)
    db.session.flush()

    return obj


# === READ ===


# ID
@handle_db_exceptions
def get_by_id(model, id, not_found_exception):
    obj = db.session.get(model, id)

    if not obj:
        raise not_found_exception()

    return obj


# ALL
@handle_db_exceptions
def get_all(model):
    data = db.session.scalars(select(model)).all()

    return data


# === UPDATE ===
def update_model(obj, data: dict):
    for field, value in data.items():
        setattr(obj, field, value)

    db.session.flush()

    return obj


# === DELETE ===
@handle_db_exceptions
def delete_model(obj):
    db.session.delete(obj)
