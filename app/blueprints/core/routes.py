from flask import Blueprint, redirect, url_for

core_bp = Blueprint("core", __name__)


@core_bp.get("/")
def root():
    return redirect(url_for("students.home"))
