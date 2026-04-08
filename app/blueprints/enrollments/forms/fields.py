from app.forms.fields import select_field, text_field


def student_id_field():
    return text_field("ID del estudiate", max_length=50)


def category_id_field():
    return select_field("Categoría")
