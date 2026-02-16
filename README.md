<h1 align="center">🚘 App – Gestión de Clases Prácticas</h1>

Aplicación web desarrollada con **Flask** para la gestión de clases prácticas
en la academia de conducción **Grand Prix**.

---

## 🧑‍💻 Entorno de desarrollo
- Python 3.12.8
- Visual Studio Code

---

## 🛠️ Tecnologías
- 🗄️ Base de datos: MySQL

- ⚙️ Backend
  - Flask
  - ORM: Flask-SQLAlchemy
  - Migraciones: Flask-Migrate
  - Variables de entorno: python-dotenv
  - Formularios: Flask-WTF
  - Mensajería: Flash
  - Logs: logging (módulo estándar de Python)

- 🎨 Frontend
  - Bootstrap (CSS / JS)
  - Bootstrap-Icons
  - Sass: preprocesador CSS
  - Gulp: automatización de tareas frontend
    - gulp-sass: compilación de archivos SCSS
    - gulp-clean-css: minificación CSS
    - gulp-terser: minificación JS
    - gulp-rename: renombrado de archivos

- 🧹 Calidad de Código
  - Black - formateo automático de código
  - Ruff - detección de errores y orden de imports
  - Pre-commit - ejecución automática de `Black` y `Ruff` antes de cada **commit**


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
# Formatear
black .

# Analizar
ruff check .
ruff check . --fix
```

## 🔒 Pre-commit
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

<h2 align="center">💡 Recomendaciones (Dev)</h2>

### 📦 Modelos (DB)
Ubicación:

```bash
app/db/models/
```

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
Ubicación:

```bash
app/blueprints/
```

Un Blueprint agrupa toda la lógica relacionada con una sección específica de la aplicación (por ejemplo: students, instructors, vehicles, etc.).

Cada blueprint debe contener:
- `routes/` → Endpoints HTTP
- `services/` → Lógica de negocio
- `forms/` → Formularios (WTForms)
- `exceptions.py` → Excepciones del dominio

Crear el blueprint en: `app/blueprints/`

Luego registrarlo en: `app/blueprints/__init__.py`

---

### ⚠️ Manejo de Excepciones
La aplicación separa las excepciones por capas:

**🔹 Globales**

Ubicación: 
```bash
app/core/exceptions.py
```

> Contiene `AppError`, la clase base para todos los errores controlados del sistema.

**🔹 Base de Datos**

Ubicación:

```bash
app/db/exceptions.py
```

**🔹 Dominio (Blueprint)**

Cada blueprint debe tener su propio archivo: `exceptions.py`

> Todas deben heredar de `AppError` para manejar mensajes personalizados.

#### 💫 Estrategia de Manejo por Capas
La aplicación implementa una estrategia de manejo de errores por niveles:

- **Services**: Deben capturar excepciones conocidas y esperadas de infraestructura (por ejemplo, errores de base de datos) y traducirlas a excepciones de dominio.

- **Routes (Blueprints)**: Deben capturar únicamente excepciones de dominio esperadas y mostrar mensajes adecuados al usuario.

- **Error Handlers globales**: Se encargan de capturar excepciones inesperadas (errores de programación o fallos no previstos) y mostrar una página 500 genérica sin exponer información sensible.

---

### 📄 Logging
La aplicación utiliza el módulo estándar `logging` de Python.

**Ubicación (configuración)**:

```bash
app/core/logging_config.py
```

**Características**:
- Logs almacenados en `logs/app.log`
- amaño máximo por archivo: 10KB
- Hasta 5 archivos de respaldo
- No se muestran logs en la terminal
- Nivel mínimo configurado: `INFO`

**Uso en módulos**

En cualquier archivo donde se necesiten logs:

```python
import logging

logger = logging.getLogger(__name__)
```

Métodos disponibles:

```python
logger.info("Informational message")
logger.warning("Business warning")
logger.error("Handled error")
logger.exception("Unexpected error")  # incluye traceback
```

#### 📌 Convenciones
- Los mensajes deben escribirse en **inglés**.
- Evitar el uso de f-strings en logging.

---

### 🎨 Vistas (Templates)
Ubicación: 

```bash
app/templates/
```

> Recomendación: Todas las vistas deben extender: `base.html`