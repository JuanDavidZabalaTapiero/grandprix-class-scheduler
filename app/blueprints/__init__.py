from .categories import categories_bp
from .core.routes import core_bp
from .instructors import instructors_bp
from .students import students_bp
from .students.api import api_bp as students_api


def register_blueprints(app):
    app.register_blueprint(core_bp)
    app.register_blueprint(students_bp)
    app.register_blueprint(instructors_bp)
    app.register_blueprint(categories_bp)

    # APIS
    app.register_blueprint(students_api)
