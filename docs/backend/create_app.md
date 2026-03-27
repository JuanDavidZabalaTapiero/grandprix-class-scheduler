# 🏭 App Factory (create_app)

La aplicación utiliza el patrón **Application Factory** de Flask.

Este patrón permite crear múltiples instancias de la aplicación con diferentes configuraciones y facilita el testing y la modularidad.

El punto de entrada principal es la función:

```python
create_app()
```

Ubicación:

```bash
app/__init__.py
```

---

# Flujo de inicialización

La creación de la aplicación sigue estos pasos:

1. Crear la instancia de Flask
2. Configurar logs
3. Cargar configuración
4. Validar configuración
5. Inicializar extensiones
6. Registrar modelos
7. Registrar blueprints
8. Registrar manejadores de errores