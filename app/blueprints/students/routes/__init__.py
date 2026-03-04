from flask import flash, redirect, url_for

from app.blueprints.students import students_bp
from app.core.exceptions import AppError


@students_bp.errorhandler(AppError)
def handle_app_error(error):
    flash(str(error), "danger")
    return redirect(url_for("students.home"))


from . import create, edit, home  # noqa
