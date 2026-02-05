# 🚘 App – Gestión de Clases Prácticas

Aplicación web desarrollada con **Flask** para la gestión de clases prácticas
en la academia de conducción **Grand Prix**.

---

## 🧑‍💻 Entorno de desarrollo
- Python 3.12.8
- Visual Studio Code

---

## 🛠️ Tecnologías
- Flask
- Black – formateo automático de código
- Ruff – detección de errores y orden de imports
- Pre-commit – ejecución automática de `Black` y `Ruff` antes de cada **commit**

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
```

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
En la raíz del proyecto, ejecutar una sola vez:

```bash
pre-commit install
```

Salida esperada:

```bash
pre-commit installed at .git\hooks\pre-commit
```

---

## ▶ Ejecutar App
En la `raíz` del proyecto, ejecutar:

```bash
py run.py
```