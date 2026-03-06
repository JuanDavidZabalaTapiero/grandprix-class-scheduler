from flask import flash

from app.extensions import db

from .exceptions import AppError


def run_service(service_func, success_message=None):
    try:
        result = service_func()

        # COMMIT
        db.session.commit()

        # MENSAJE
        flash(success_message, "success")

        return result

    except AppError as e:
        db.session.rollback()
        flash(str(e), "danger")

        # MANEJO EN RUTA
        raise
