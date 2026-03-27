# ⚙️ Configuración de la aplicación

La configuración del proyecto se define en:

```bash
app/config.py
```

---

# Variables de entorno

Se utilizan variables de entorno para evitar almacenar información sensible en el código.

La librería utilizada es:

```python
python-dotenv
```

Esto permite cargar automáticamente las variables desde un archivo `.env`.

---

# Variables requeridas

El archivo `.env` debe contener al menos:

```env
SECRET_KEY=mi_llave_secreta
DATABASE_URL=mysql+mysqldb://user:pass@host/db_name
```

Estas variables son validadas al iniciar la aplicación para evitar errores de configuración.