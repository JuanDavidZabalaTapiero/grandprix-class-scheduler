from datetime import date

from flask import Blueprint, jsonify, render_template, request

from .services import count_sales

sales_bp = Blueprint("sales", __name__, url_prefix="/sales")


@sales_bp.get("/")
def enrollments():
    today = date.today()
    return render_template("sales/enrollments.html", today=today)


@sales_bp.get("/get")
def get_sales():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    sales = count_sales(start_date, end_date)
    return jsonify(sales)
