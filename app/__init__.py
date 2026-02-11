from flask import Flask, render_template

from .blueprints import register_blueprints
from .config import Config
from .extensions import csrf, db, migrate


def create_app():
    app = Flask(__name__)

    # == CONFIG ==
    app.config.from_object(Config)

    # == INICIALIZAR EXTENSIONES ==
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # == IMPORTAR MODELOS (MIGRACIONES) ==
    from app.db import models  # noqa: F401

    # == REGISTRAR BLUEPRINTS ==
    register_blueprints(app)

    # == ERRORES ==

    # 404
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html")

    return app
