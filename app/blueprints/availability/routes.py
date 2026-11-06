from flask import Blueprint, render_template

from .utils import get_availability_grids

availability_bp = Blueprint("availability", __name__, url_prefix="/availability")


@availability_bp.get("/")
def home():
    grids = get_availability_grids()
    return render_template("availability/home.html", grids=grids)
