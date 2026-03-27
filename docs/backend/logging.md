# 📜 Sistema de Logs

La aplicación implementa un sistema de logging centralizado para registrar eventos importantes, errores y comportamiento del sistema.

Ubicación de la configuración:

```bash
app/core/logging_config.py
```

El sistema utiliza el módulo estándar de Python:

```python
logging
```

y un manejador de archivos rotativo:

```python
RotatingFileHandler
```

---

# Directorio de logs

Los logs se almacenan dentro del directorio:

```bash
instance/logs/
```

Archivo principal:

```bash
app.log
```

Configuración:

- Tamaño máximo por archivo: **1MB**
- Número máximo de backups: **5**

Esto evita que los logs crezcan indefinidamente.

---

# Objetivo del sistema de logs

Permite registrar:

- errores de aplicación
- errores HTTP
- fallos de base de datos
- eventos relevantes

Esto facilita el **debugging**, monitoreo y auditoría del sistema.