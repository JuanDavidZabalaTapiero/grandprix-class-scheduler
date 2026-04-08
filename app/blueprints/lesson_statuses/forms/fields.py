from app.forms.fields import text_field


def name_field():
    return text_field("Nombre", max_length=20)
