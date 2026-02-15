from .core.routes import core_bp
from .students import students_bp


def register_blueprints(app):
    app.register_blueprint(core_bp)
    app.register_blueprint(students_bp)
