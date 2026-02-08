from .students.routes import students_bp
from .tests.routes import tests_bp


def register_blueprints(app):
    app.register_blueprint(tests_bp)
    app.register_blueprint(students_bp)
