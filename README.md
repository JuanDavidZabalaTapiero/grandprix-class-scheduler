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

## Ejecutar App
En la `raíz` del proyecto, ejecutar:

```bash
py run.py
```