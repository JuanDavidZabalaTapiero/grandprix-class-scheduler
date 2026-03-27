# 🧾 Formularios

Los formularios del proyecto se implementan utilizando:

```bash
Flask-WTF
```

Esto permite integrar **WTForms** con Flask y agregar protección **CSRF** automáticamente.

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

---

# Protección CSRF

Flask-WTF incluye protección CSRF automáticamente mediante:

```bash
CSRFProtect
```

La extensión se inicializa en:

```bash
app/extensions.py
```

Esto protege los formularios contra ataques de falsificación de solicitudes.