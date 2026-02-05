from flask import Blueprint, render_template

test_bp = Blueprint("tests", __name__, url_prefix="/tests")


@test_bp.get("/")
def home():
    return render_template("test/home.html")
