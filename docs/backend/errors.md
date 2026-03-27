# ⚠️ Manejo de errores

La aplicación implementa una arquitectura de errores basada en **excepciones personalizadas** para separar los errores de negocio, infraestructura y HTTP.

---

# Tipos de errores

La aplicación distingue varios tipos de errores:

1️⃣ Errores de aplicación  
2️⃣ Errores de base de datos  
3️⃣ Errores HTTP  
4️⃣ Errores inesperados

Todos los errores se manejan centralmente en:

```bash
app/core/error_handlers.py
```

---

# Error base de la aplicación

Ubicación:

```bash
app/core/exceptions.py
```

```python
class AppError(Exception):

    default_message = "Ocurrió un error inesperado. Vuelva a intentar más tarde."
    status_code = 400

    def __init__(self, message=None):
        super().__init__(message or self.default_message)
```

Este error actúa como **clase base para todas las excepciones del dominio**.

---

# Manejo centralizado de errores

Los manejadores se registran en la aplicación:

```python
register_error_handlers(app)
```

---

# Error de aplicación

Cuando ocurre un `AppError`:

- se registra el evento en logs
- se muestra un mensaje flash al usuario
- se redirige a la página principal

```python
@app.errorhandler(AppError)
```

---

# Error CSRF

Los errores de validación CSRF son manejados separadamente.

```python
@app.errorhandler(CSRFError)
```

---

# Errores HTTP

Los errores HTTP utilizan templates específicos.

```python
@app.errorhandler(HTTPException)
```

Ejemplos de páginas disponibles:

```bash
templates/errors/
 ├── 400.html
 ├── 401.html
 ├── 403.html
 ├── 404.html
 ├── 405.html
 ├── 500.html
 └── generic_http.html
```

---

# Errores inesperados

Si ocurre una excepción no controlada:

```python
@app.errorhandler(Exception)
```

Esto evita que el usuario vea errores internos del servidor.