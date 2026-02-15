import logging

from flask import render_template
from flask_wtf.csrf import CSRFError


def register_error_handlers(app):

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(CSRFError)
    def handle_csrf_error(error):
        logger = logging.getLogger(__name__)
        logger.warning(
            "CSRF validation failed | reason=%s",
            error.description,
        )

        return render_template("errors/csrf.html"), 400

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        logger = logging.getLogger(__name__)
        logger.exception("Unhandled exception occurred")

        return render_template("errors/500.html"), 500
