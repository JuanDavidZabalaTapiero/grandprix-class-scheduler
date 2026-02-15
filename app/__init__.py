from flask import Flask

from app.core.error_handlers import register_error_handlers
from app.core.logging_config import configure_logging

from .blueprints import register_blueprints
from .config import Config
from .extensions import csrf, db, migrate

# =========================
# CONFIG VALIDATION
# =========================


def validate_config(app: Flask) -> None:
    if not app.config.get("SECRET_KEY"):
        raise RuntimeError("SECRET_KEY is not configured")

    if not app.config.get("SQLALCHEMY_DATABASE_URI"):
        raise RuntimeError("SQLALCHEMY_DATABASE_URI is not configured")


# =========================
# APP FACTORY
# =========================


def create_app() -> Flask:
    app = Flask(__name__)

    # === LOGS ===
    configure_logging()

    # === CONFIG ===
    app.config.from_object(Config)
    validate_config(app)  # FAIL-FAST

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
