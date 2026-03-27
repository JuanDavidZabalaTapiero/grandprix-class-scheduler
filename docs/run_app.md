# 💫 Ejecutar App

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

## 🎮 Iniciar aplicación
En la `raíz` del proyecto, ejecutar:

```bash
python run.py
```