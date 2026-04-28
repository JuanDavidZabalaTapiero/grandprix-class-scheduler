from datetime import time


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
