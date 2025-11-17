# Análisis actual de funcionalidades

Grupo: GLHF

Fecha: 2025-11-17

Resumen:

Este repositorio contiene una aplicación de escritorio (Tkinter) que gestiona una base de datos MySQL con las tablas libros, prestamos, usuarios y reportes. La estructura se ha reorganizado para seguir un enfoque modular: cada funcionalidad vive en su propio archivo dentro del paquete `features/` y `main.py` actúa como lanzador de la interfaz gráfica.

Funcionalidades implementadas actualmente:

- Conexión centralizada a la DB en `db.py`.
- Operaciones CRUD básicas sobre `libros` (seleccionar, agregar, eliminar, buscar) en `features/libros.py`.
- Gestión de préstamos (prestar, devolver, obtener vencidos) en `features/prestamos.py`.
- Generación de reportes en `features/reportes.py`.
- Visualización en GUI desde `main.py` con ventanas para agregar, prestar y devolver.
- Corrección del formato de fechas en las consultas (DATE_FORMAT con '%Y-%m-%d').

Limitaciones actuales / Riesgos:

- No hay control de roles ni autenticación real; cualquier usuario puede ejecutar acciones que afectan el inventario.
- El campo "prestamos" en la tabla se construye como un GROUP_CONCAT; para libros con muchos préstamos puede saturarse la celda de la tabla.
- No hay pruebas automatizadas ni CI configurado aún.
- Configuración de la base de datos disponible en `config.py` como placeholders — no subir credenciales públicas.

Prioridades inmediatas:

1. Implementar exportación de datos (CSV/PDF) para reportes comerciales.
2. Añadir funciones estadísticas para análisis rápido (conteos, top-usuarios).
3. Implementar vistas detalladas de préstamos por libro y acciones rápidas (marcar devuelto).
4. Introducir autenticación/roles (bibliotecario/administrador) y logging de auditoría.