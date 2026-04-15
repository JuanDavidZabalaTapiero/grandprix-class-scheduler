from .base import BaseSchema


class LessonTypeSchema(BaseSchema):
    fields = ["name", "is_default"]
