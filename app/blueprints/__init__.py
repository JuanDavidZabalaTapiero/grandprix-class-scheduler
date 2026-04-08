from .categories import categories_bp
from .core.routes import core_bp
from .enrollments import enrollments_bp
from .instructor_vehicles import instructor_vehicles_bp
from .instructors import instructors_bp
from .lesson_statuses import lesson_statuses_bp
from .lesson_types import lesson_types_bp
from .students import students_bp
from .students.api import api_bp as students_api
from .vehicles import vehicles_bp


def register_blueprints(app):
    app.register_blueprint(core_bp)
    app.register_blueprint(students_bp)
    app.register_blueprint(instructors_bp)
    app.register_blueprint(categories_bp)
    app.register_blueprint(vehicles_bp)
    app.register_blueprint(enrollments_bp)
    app.register_blueprint(instructor_vehicles_bp)
    app.register_blueprint(lesson_types_bp)
    app.register_blueprint(lesson_statuses_bp)

    # APIS
    app.register_blueprint(students_api)
