from flask import Blueprint, render_template

students_bp = Blueprint("students", __name__)


@students_bp.get("/")
def home():
    return render_template("students/home.html")
