class StudentSchema:
    fields = ["document_id", "name", "phone"]

    @classmethod
    def load(cls, data: dict) -> dict:
        return {field: data.get(field) for field in cls.fields}
