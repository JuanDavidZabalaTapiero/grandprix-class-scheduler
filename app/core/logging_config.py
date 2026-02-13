import logging
import os
from logging.handlers import RotatingFileHandler


def configure_logging(app):

    # CREAR CARPETA LOGS/ EN RAÍZ
    if not os.path.exists("logs"):
        os.mkdir("logs")

    # === FILEHANDLER ===

    # ELIMINAR HANDLERS POR DEFECTO
    app.logger.handlers.clear()

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = RotatingFileHandler("logs/app.log", maxBytes=10240, backupCount=5)

    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # AÑADIR A FLASK
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.propagate = False
