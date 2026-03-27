# 🔌 Extensiones de Flask

Las extensiones se inicializan en un módulo separado para evitar dependencias circulares y facilitar la reutilización.

Ubicación:

```bash
app/extensions.py
```

---

# Extensiones utilizadas

## SQLAlchemy

ORM utilizado para interactuar con la base de datos.

```python
db = SQLAlchemy()
```

---

## Flask-Migrate

Permite gestionar migraciones de base de datos utilizando **Alembic**.

```python
migrate = Migrate()
```

---

## CSRFProtect

Protege los formularios contra ataques **Cross-Site Request Forgery**.

```python
csrf = CSRFProtect()
```

---

# Inicialización en la aplicación

Las extensiones se inicializan dentro del **App Factory**.

```python
db.init_app(app)
migrate.init_app(app, db)
csrf.init_app(app)
```