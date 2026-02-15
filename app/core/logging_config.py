import logging
import os
import re
from logging.handlers import RotatingFileHandler


# DESACTIVAR CÓDIGO ANSI
class NoColorFormatter(logging.Formatter):
    ANSI_ESCAPE = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")

    def format(self, record):
        message = super().format(record)
        return self.ANSI_ESCAPE.sub("", message)


# === CONFIG LOGS ===
def configure_logging():

    # CREAR CARPETA LOGS/ EN RAÍZ
    os.makedirs("logs", exist_ok=True)
    log_path = os.path.abspath("logs/app.log")

    formatter = NoColorFormatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # VERIFICAR SI YA EXISTE UN ROTATINGFILEHANDLER
    for handler in root_logger.handlers:
        if (
            isinstance(handler, RotatingFileHandler)
            and os.path.abspath(handler.baseFilename) == log_path
        ):
            return  # YA ESTÁ CONFIGURADO -> SALIR

    file_handler = RotatingFileHandler(log_path, maxBytes=10240, backupCount=5)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    root_logger.addHandler(file_handler)
