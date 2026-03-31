# 📦 Creación de un CRUD

Este documento describe el flujo estándar para implementar un CRUD completo (Create, Read, Update, Delete) para un nuevo modelo dentro del proyecto.

Se asume que el modelo ya existe en la base de datos y que la migración correspondiente ha sido aplicada correctamente.

---

## 🧩 Estructura general

El CRUD se construye siguiendo una arquitectura modular basada en componentes clave:

- Blueprints
- Schemas (BaseSchema)
- Excepciones (AppError)
- Formularios (ModelForm)
- Servicios (CRUDServices)
- Rutas reutilizables (CRUDRoutes)
- Templates

Este enfoque permite mantener el sistema desacoplado, reutilizable y escalable.

---

## 🧱 1. Blueprint

Se debe crear un blueprint para el nuevo modelo: `app/blueprints/`

Responsabilidades:
- Agrupar la lógica del módulo
- Definir un prefijo de URL
- Registrar las rutas del módulo

También debe registrarse globalmente en la aplicación: `app/blueprints/__init__.py`.

---

## 🧾 2. Schema (BaseSchema)

Los schemas heredan de **BaseSchema**.

Su función es:
- Definir qué campos son válidos
- Filtrar los datos provenientes del formulario
- Estandarizar la entrada de datos hacia los servicios

Esto evita que datos no deseados lleguen a la lógica de negocio.

---

## ⚠️ 3. Excepciones (AppError)

Las excepciones del módulo deben heredar de **AppError**.

Permiten:
- Manejar errores de negocio de forma controlada
- Definir mensajes y códigos HTTP personalizados

Ejemplo de uso:
- “Entidad no encontrada”
- Validaciones específicas del dominio

También existen excepciones globales para errores de base de datos.

---

## 📝 4. Formularios (ModelForm)

Los formularios heredan de **ModelForm**.

Se dividen en:

### a) Campos reutilizables
- Definen validaciones
- Aplican normalización de datos

### b) Formulario del modelo
- Agrupa los campos necesarios
- Permite convertir los datos a un formato procesable

El formulario se encarga de:
- Validar entrada del usuario
- Preparar datos para el schema

---

## 🧠 5. Servicios (CRUDServices)

Los servicios heredan de **CRUDServices**, que provee operaciones base:

- Crear
- Obtener por ID
- Listar
- Actualizar
- Eliminar

Responsabilidades:
- Contener la lógica de negocio
- Interactuar con la base de datos
- Lanzar excepciones cuando sea necesario

También integran manejo de errores de base de datos mediante decoradores.

---

## 🔀 6. Rutas (CRUDRoutes)

Las rutas CRUD se generan automáticamente usando **CRUDRoutes**.

Este componente:
- Registra endpoints dinámicamente
- Conecta formularios, schemas y servicios
- Reduce código repetitivo

Operaciones disponibles:
- Listado
- Creación
- Edición
- Eliminación

Todas son opcionales y configurables.

---

## 🎨 7. Templates

### a) Listado
Layout: `templates/layouts/home_page.html`

Muestra:
- Tabla de registros
- Botones de editar y eliminar
- Botón para crear

### b) Formulario (crear / editar)
Base: `templates/forms/entity_form.html`

- Se reutiliza un solo template
- Incluye inputs modulares
- Maneja estados de carga

---

## 🔄 Flujo completo

1. Usuario accede al listado
2. Puede crear, editar o eliminar registros
3. En formularios:
   - Se valida la información
   - Se filtra con BaseSchema
   - Se ejecuta el servicio (CRUDServices)
4. Se maneja la transacción
5. Se redirige con mensaje de éxito

---

## ⚙️ Buenas prácticas

- La lógica de negocio debe ir en servicios (CRUDServices)
- Las rutas (CRUDRoutes) solo coordinan el flujo
- Los schemas (BaseSchema) controlan la entrada de datos
- Los formularios (ModelForm) validan la entrada del usuario
- Las excepciones (AppError) manejan errores de dominio

---

## 🚀 Flexibilidad

El sistema permite:

- Omitir operaciones CRUD innecesarias
- Crear rutas personalizadas fuera de CRUDRoutes
- Reutilizar lógica entre múltiples modelos

---

Este enfoque permite implementar CRUDs de forma rápida, consistente y escalable dentro del proyecto.
