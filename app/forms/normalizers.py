import re


def normalize_name(value: str) -> str:
    if value:
        value = value.strip()
        value = re.sub(r"\s+", " ", value)
        return value.upper()
    return value


def normalize_phone(value: str) -> str:
    if value:
        return value.strip()
    return value
