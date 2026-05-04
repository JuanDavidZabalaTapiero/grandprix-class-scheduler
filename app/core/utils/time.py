from datetime import date, datetime, time

DAYS_ES = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
MONTHS_ES = [
    "enero",
    "febrero",
    "marzo",
    "abril",
    "mayo",
    "junio",
    "julio",
    "agosto",
    "septiembre",
    "octubre",
    "noviembre",
    "diciembre",
]


def format_time(t: time) -> str:
    hour = t.hour
    minute = t.minute

    suffix = "a.m." if hour < 12 else "p.m."

    # FORMATO 12H
    hour_12 = hour % 12

    # CASO ESPECIAL
    if hour_12 == 0:
        hour_12 = 12

    return f"{hour_12}:{minute:02d} {suffix}"


def format_date_spanish(d) -> str:

    # -------------------------
    # NORMALIZAR INPUT
    # -------------------------
    if isinstance(d, str):
        d = datetime.strptime(d, "%Y-%m-%d").date()
    elif isinstance(d, datetime):
        d = d.date()
    elif not isinstance(d, date):
        raise ValueError("Formato de fecha no válido")

    # -------------------------
    # COMPONENTES
    # -------------------------
    day_name = DAYS_ES[d.weekday()]  # 0 = lunes
    day_number = d.day
    month_name = MONTHS_ES[d.month - 1]
    year = d.year

    # Capitalizar primera letra del día
    day_name = day_name.capitalize()

    return f"{day_name}, {day_number} de {month_name} de {year}"
