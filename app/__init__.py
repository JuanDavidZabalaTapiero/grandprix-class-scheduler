from flask import Flask

from app.core.error_handlers import register_error_handlers
from app.core.logging_config import configure_logging

from .blueprints import register_blueprints
from .config import Config
from .extensions import csrf, db, migrate


def create_app():
    app = Flask(__name__)

    # === LOGS ===
    configure_logging()

    # === CONFIG ===
    app.config.from_object(Config)

    # === EXTENSIONES ===
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # === MODELOS (MIGRACIONES) ===
    from app.db import models  # noqa: F401

    # === BLUEPRINTS ===
    register_blueprints(app)

    # === ERRORES ===
    register_error_handlers(app)

    return app
