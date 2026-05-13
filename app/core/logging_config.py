import logging
import re
from pathlib import Path

from concurrent_log_handler import ConcurrentRotatingFileHandler


# DESACTIVAR CÓDIGO ANSI
class NoColorFormatter(logging.Formatter):
    ANSI_ESCAPE = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")

    def format(self, record):
        message = super().format(record)
        return self.ANSI_ESCAPE.sub("", message)


# === CONFIG LOGS ===
def configure_logging(app):

    # DIRECTORIO DE LOGS
    logs_dir = Path(app.instance_path) / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

    log_path = logs_dir / "app.log"

    formatter = NoColorFormatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # EVITAR DUPLICADOS
    for handler in root_logger.handlers:
        if (
            isinstance(handler, ConcurrentRotatingFileHandler)
            and Path(handler.baseFilename) == log_path
        ):
            return

    file_handler = ConcurrentRotatingFileHandler(
        log_path,
        maxBytes=1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )

    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    root_logger.addHandler(file_handler)
