import logging

from flask import render_template
from flask_wtf.csrf import CSRFError
from jinja2 import TemplateNotFound
from werkzeug.exceptions import HTTPException

logger = logging.getLogger(__name__)


def register_error_handlers(app):

    # === CSRF ===
    @app.errorhandler(CSRFError)
    def handle_csrf_error(error):
        logger.warning(
            "CSRF validation failed | reason=%s",
            error.description,
        )

        return render_template("errors/csrf.html"), 400

    # === HTTP ===
    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        logger.warning(
            "HTTP exception occurred | code=%s | description=%s",
            error.code,
            error.description,
        )

        try:
            return render_template(f"errors/{error.code}.html"), error.code
        except TemplateNotFound:
            return (
                render_template("errors/generic_http.html", code=error.code),
                error.code,
            )

    # === EXCEPTION ===
    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        logger.exception("Unhandled exception occurred")

        return render_template("errors/500.html"), 500
