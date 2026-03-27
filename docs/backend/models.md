# 🗄️ Modelos de base de datos

Los modelos representan las tablas de la base de datos utilizando **SQLAlchemy ORM**.

Ubicación:

```bash
app/db/models/
```

---

# Estructura recomendada

Cada modelo se define en su propio archivo:

```bash
app/db/models/
 ├── student.py
 ├── instructor.py
 └── __init__.py
```

El archivo `__init__.py` debe importar los modelos para que **Flask-Migrate pueda detectarlos**.

Ejemplo:

```python
from .instructor import Instructor
from .student import Student

__all__ = ["Student", "Instructor"]
```

---

# Migraciones de base de datos

Las migraciones permiten actualizar la estructura de la base de datos de forma controlada.

Se gestionan con:

```bash
Flask-Migrate
```

---

# Crear una migración

```bash
flask db migrate -m "mensaje descriptivo"
```

Ejemplo:

```bash
flask db migrate -m "create students table"
```

---

# Aplicar migraciones

```bash
flask db upgrade
```

Esto sincroniza la base de datos con los modelos definidos en el proyecto.

---

# Recomendaciones

- Crear una migración cada vez que cambie un modelo
- Utilizar mensajes descriptivos
- Revisar el archivo generado antes de aplicarlo