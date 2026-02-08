from flask import Blueprint, render_template

tests_bp = Blueprint("tests", __name__, url_prefix="/tests")


@tests_bp.get("/")
def home():
    return render_template("tests/home.html")
