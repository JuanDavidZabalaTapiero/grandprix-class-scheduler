import logging
import re
from logging.handlers import RotatingFileHandler
from pathlib import Path


# DESACTIVAR CÓDIGO ANSI
class NoColorFormatter(logging.Formatter):
    ANSI_ESCAPE = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")

    def format(self, record):
        message = super().format(record)
        return self.ANSI_ESCAPE.sub("", message)


# === CONFIG LOGS ===
def configure_logging(app):

    # == DIRECTORIO DE LOGS ==
    logs_dir = Path(app.instance_path) / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)  # CREAR CARPETA

    log_path = logs_dir / "app.log"

    # == CONFIG ==
    formatter = NoColorFormatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # VERIFICAR SI YA EXISTE UN ROTATINGFILEHANDLER
    for handler in root_logger.handlers:
        if (
            isinstance(handler, RotatingFileHandler)
            and Path(handler.baseFilename) == log_path
        ):
            return  # YA ESTÁ CONFIGURADO -> SALIR

    file_handler = RotatingFileHandler(
        log_path, maxBytes=1024 * 1024, backupCount=5, delay=True
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    root_logger.addHandler(file_handler)
