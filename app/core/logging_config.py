import logging
import os
import re
from logging.handlers import RotatingFileHandler


# DESACTIVAR CÓDIGO ANSI
class NoColorFormatter(logging.Formatter):
    def format(self, record):
        message = super().format(record)
        ansi_escape = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")
        return ansi_escape.sub("", message)


# === CONFIG LOGS ===
def configure_logging():

    # CREAR CARPETA LOGS/ EN RAÍZ
    os.makedirs("logs", exist_ok=True)

    # === FILEHANDLER ===
    formatter = NoColorFormatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

    file_handler = RotatingFileHandler("logs/app.log", maxBytes=10240, backupCount=5)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # === ROOT LOGGER ===
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)
