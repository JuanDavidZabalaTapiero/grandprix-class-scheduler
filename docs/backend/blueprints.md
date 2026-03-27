# 🧩 Blueprints

Los **Blueprints** permiten dividir una aplicación Flask en componentes reutilizables.

Cada blueprint agrupa:

- rutas
- templates
- formularios
- lógica relacionada

Esto facilita mantener proyectos grandes.

---

# Registro de blueprints

Los blueprints se registran dentro de la función de creación de la aplicación.

Ubicación:

```bash
app/blueprints/__init__.py
```

Ejemplo:

```python
from .instructors import instructors_bp
from .students import students_bp


def register_blueprints(app):
    app.register_blueprint(students_bp)
    app.register_blueprint(instructors_bp)
```

---

# Ventajas

El uso de blueprints permite:

- modularizar la aplicación
- separar responsabilidades
- facilitar mantenimiento
- reutilizar componentes
- mejorar la organización del código