# 🎨 Sistema de Plantillas

La interfaz del proyecto utiliza el motor de plantillas:

```bash
Jinja2
```

Jinja2 permite generar HTML dinámico a partir de datos enviados desde las rutas.

Ubicación de las plantillas:

```bash
app/templates/
```

---

# Estructura de plantillas

Ejemplo:

```bash
app/templates/
 ├── base.html
 ├── layouts/
 ├── macros/
 ├── components/ 
 ├── students/
 │   └── home.html
 └── instructors/
```

Cada módulo tiene su propio directorio de templates.

Esto facilita mantener organizada la interfaz.

---

# Plantilla base

Normalmente todas las páginas heredan de una plantilla base.

```html
{% extends "base.html" %}
```
