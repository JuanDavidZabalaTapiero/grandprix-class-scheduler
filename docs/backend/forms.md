# 🧾 Formularios

Los formularios del proyecto se implementan utilizando:

```bash
Flask-WTF
```

Esto permite integrar **WTForms** con Flask.

---

# BaseForm

El proyecto utiliza un formulario base que permite centralizar configuraciones comunes.

```python
class BaseForm(FlaskForm):
```

Esto permite extender fácilmente los formularios del sistema.

---

# Ejemplo de formulario

Ejemplo de formulario para estudiantes:

```python
class StudentForm(BaseForm):

    name = StringField(
        "Nombre",
        validators=[DataRequired()]
    )

    email = StringField(
        "Correo",
        validators=[DataRequired(), Email()]
    )

    submit = SubmitField("Guardar")
```

---

# Validación de formularios

Los formularios se validan normalmente dentro de las rutas:

```python
form = StudentForm()

if form.validate_on_submit():
    data = form.data
```
