from .core.routes import core_bp
from .students import students_bp
from .students.api import api_bp as students_api


def register_blueprints(app):
    app.register_blueprint(core_bp)
    app.register_blueprint(students_bp)

    # APIS
    app.register_blueprint(students_api)
