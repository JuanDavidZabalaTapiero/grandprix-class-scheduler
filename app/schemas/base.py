class BaseSchema:
    fields = []

    @classmethod
    def load(cls, data: dict) -> dict:
        return {field: data.get(field) for field in cls.fields}
