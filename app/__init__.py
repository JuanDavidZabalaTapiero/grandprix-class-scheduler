from flask import Flask

from .blueprints import register_blueprints
from .config import Config
from .extensions import db, migrate


def create_app():
    app = Flask(__name__)

    # == CONFIG ==
    app.config.from_object(Config)

    # == INICIALIZAR EXTENSIONES ==
    db.init_app(app)
    migrate.init_app(app, db)

    # == IMPORTAR MODELOS (MIGRACIONES) ==
    from app.db import models  # noqa: F401

    # == REGISTRAR BLUEPRINTS ==
    register_blueprints(app)

    return app
