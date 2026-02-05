from .test.routes import test_bp


def register_blueprints(app):
    app.register_blueprint(test_bp)
