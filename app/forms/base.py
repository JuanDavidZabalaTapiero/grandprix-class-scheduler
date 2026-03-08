from flask_wtf import FlaskForm


class ModelForm(FlaskForm):

    def to_dict(self):
        data = {}

        for (
            name,
            field,
        ) in self._fields.items():
            if name not in ("csrf_token", "submit"):
                data[name] = field.data

        return data
