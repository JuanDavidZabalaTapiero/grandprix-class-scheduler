# 🚘 App – Gestión de Clases Prácticas

Aplicación web desarrollada con **Flask** para la gestión de clases prácticas
en la academia de conducción **Grand Prix**.

---

## 🧑‍💻 Entorno de desarrollo
- Python 3.12.8
- Visual Studio Code

---

## 🛠️ Tecnologías
- BD: MySQL

- Backend
  - Flask
  - ORM: Flask-SQLAlchemy
  - Migraciones: Flask-Migrate
  - Variables de entorno: python-dotenv
  - Formularios: Flask-WTF

- Calidad de Código
  - Black - formateo automático de código
  - Ruff - detección de errores y orden de imports
  - Pre-commit - ejecución automática de `Black` y `Ruff` antes de cada **commit**
  
- Frontend
  - Bootstrap (CSS / JS)
  - Bootstrap-Icons
  - Sass: preprocesador CSS
  - Gulp: automatización de tareas frontend
    - gulp-sass: compilación de archivos SCSS
    - gulp-clean-css: minificación CSS
    - gulp-terser: minificación JS
    - gulp-rename: renombrado de archivos

---

## 🐍 Crear y activar entorno virtual

En la `raíz` del proyecto:

### Windows
```bash
python -m venv .venv # Crear
.venv\Scripts\activate # Activar
```

### Linux / macOS
```bash
python3 -m venv .venv # Crear
source .venv/bin/activate # Activar
```

---

## 📦 Instalar dependencias
En la `raíz` del proyecto:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt # desarrollo
```

---

## 🔑 Variables de entorno

En la `raíz` del proyecto, crea un archivo llamado `.env` y define las siguientes variables:

```.env
SECRET_KEY=mi_llave_secreta
DATABASE_URL=mysql+mysqldb://user:pass@host/db_name
```
> Asegúrate de reemplazar los valores de ejemplo con los correspondientes a tu entorno de desarrollo.

---

##  🎨 Frontend (Dev)

En la carpeta `frontend` del proyecto:

```bash
npm install # Instalar dependencias
npx gulp # Ejecutar gulp (watch)
```
> Requiere Node.js y npm instalados.

---

## 🎨 Formateo y análisis de código

```bash
# Black
black .

# Ruff
ruff check .
ruff check . --fix
```

## 🔒 Automatización con pre-commit
El proyecto utiliza pre-commit para ejecutar automáticamente
`Black` y `Ruff` antes de cada commit.

### Inicializar pre-commit
En la `raíz` del proyecto, ejecutar una sola vez:

```bash
pre-commit install
```

Salida esperada:

```bash
pre-commit installed at .git\hooks\pre-commit
```

---

## 🎮 Ejecutar App
En la `raíz` del proyecto, ejecutar:

```bash
python run.py
```

---

## </> Recomendaciones (Dev)

### 📦 Modelos (DB)
Para agregar un nuevo modelo:
1. Crear el archivo dentro de: `app/db/models/`
2. Registrar el modelo en: `app/db/models/__init__.py`

> Esto es necesario para que Alembic detecte los cambios correctamente.

---

### 🔄 Migraciones
Después de crear o modificar un modelo:

```bash
flask db migrate -m "mensaje descriptivo" # Crear migración
flask db upgrade # Aplicar migración
```

---

### 🧩 Blueprints
Un Blueprint agrupa toda la lógica relacionada con una sección específica de la aplicación (por ejemplo: students, instructors, vehicles, etc.).

Cada blueprint debe contener:
- `routes.py` → Endpoints HTTP
- `services/` → Lógica de negocio
- `forms/` → Formularios (WTForms)
- `exceptions.py` → Excepciones del dominio

Crear el blueprint en: `app/blueprints/`

Luego registrarlo en: `app/blueprints/__init__.py`

---

### ⚠️ Manejo de Excepciones
La aplicación separa las excepciones por capas:

**🔹Excepciones Globales**

Ubicación: 
```bash
app/core/exceptions.py
```

> Contiene `AppError`, la clase base para todos los errores controlados del sistema.

**🔹Excepciones de Base de Datos**

Ubicación: 

```bash
app/db/exceptions.py
```

**🔹Excepciones de Dominio (Blueprint)**

Cada blueprint debe tener su propio archivo: `exceptions.py`

> Todas deben heredar de `AppError` para manejar los mensajes personalizados.

---

### 🎨 Vistas (Templates)
Ubicación: `app/templates/`

Recomendaciones:
- Todas las vistas deben extender `base.html`.


