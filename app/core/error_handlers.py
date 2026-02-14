import logging

from flask import render_template


def register_error_handlers(app):

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        logger = logging.getLogger(__name__)
        logger.exception("Unhandled exception occurred")

        return render_template("errors/500.html"), 500
