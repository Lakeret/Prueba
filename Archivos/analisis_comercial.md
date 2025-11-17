# Análisis de elementos faltantes para comercialización

Grupo: GLHF

Fecha: 2025-11-17

Resumen ejecutivo:
Este documento identifica los elementos que actualmente faltan en el proyecto para convertirlo en un producto comercializable, prioriza las mejoras, y propone artefactos y archivos necesarios. El objetivo es facilitar una hoja de ruta técnica y comercial clara para pasar de una POC/APP local a una solución lista para clientes (bibliotecas, instituciones educativas).

1) Producto y funcionalidades faltantes (Prioridad: Alta)
- Autenticación y autorización (roles: administrador, bibliotecario, usuario): imprescindible para control de acceso y facturación. Artefacto: features/auth.py, UI login en main.py, tabla usuarios_roles.
- API REST pública: exponer endpoints para catálogo, reservas y préstamos. Artefacto: features/api.py o carpeta api/, documentación OpenAPI/Swagger.
- Reservas en línea y gestión de colas: permitir que usuarios reserven ejemplares.
- Notificaciones: envío de emails/SMS para vencimientos y confirmaciones. Integración con proveedores (SendGrid, Twilio).

2) Seguridad y cumplimiento (Prioridad: Alta)
- Gestión segura de credenciales: no hardcodear, usar variables de entorno y secrets en CI/CD y GitHub. Archivo: .env.example, instrucciones en README.
- Encriptación en tránsito y en reposo para datos sensibles, políticas de backups y retención.
- Auditoría y logging (quién hizo qué y cuándo). Artefacto: logging/audit module, tabla audit_log.
- GDPR / protección de datos: políticas y mecanismos para borrado/anonimización. Archivo: archivo/legal_privacy.md.

3) Infraestructura y despliegue (Prioridad: Alta)
- Contenerización: Dockerfile y docker-compose para despliegue local y producción.
- Pipeline CI/CD: .github/workflows/ci.yml y cd.yml para tests, lint y despliegues automáticos.
- Backup / restore automatizado: scripts en ops/backup.sh y jobs cron.
- Configuración de base de datos gestionable (migrations): añadir migraciones con herramienta (Flyway, Alembic) o scripts SQL en migrations/.

4) Calidad y pruebas (Prioridad: Alta)
- Suite de pruebas: unitarias para features/ y tests de integración que verifiquen la interacción con una base de datos de prueba (tests/).
- Linter y format (flake8, black). Archivo: pyproject.toml o setup.cfg.

5) Documentación y onboarding (Prioridad: Alta)
- Documentación de API (OpenAPI), guía de instalación paso a paso, y README ampliado.
- Documentos informativos en carpeta archivo/: archivo/onboarding.md, archivo/legal_privacy.md, archivo/pricing.md.
- Ejemplos de datos y script para cargar datos de muestra (seed_data/).

6) Comercial y modelo de negocio (Prioridad: Media)
- Plan de precios y licencias: clarificar licencia (LICENSE) y modelo (SaaS, licencia por instancia, soporte).
- Asociaciones y mercado objetivo: paquetes para bibliotecas pequeñas vs. grandes instituciones.
- Integración de pago para multas/servicios: features/payments.py y acuerdos con proveedores.

7) UX / Producto (Prioridad: Media)
- Interfaz web ligera + mobile (API + frontend): permitir acceso remoto y reservas.
- Mejora de la UI de escritorio (internacionalización, accesibilidad).

8) Operaciones y soporte (Prioridad: Media)
- Monitorización y alertas (Prometheus/ Grafana o servicios gestionados).
- SLA, canales de soporte y onboarding para clientes.

Artefactos y archivos recomendados a crear inmediatamente:
- features/auth.py (login, roles, verificación).
- features/api.py + api/openapi.yaml (endpoints básicos).
- Dockerfile y docker-compose.yml.
- .github/workflows/ci.yml (tests, lint) y cd.yml (despliegue manual).
- migrations/ (scripts SQL o migrator config).
- tests/ (test_libros.py, test_prestamos.py).
- archivo/onboarding.md, archivo/legal_privacy.md, archivo/pricing.md, LICENSE, CONTRIBUTING.md.

Roadmap sugerido (sprints):
- Sprint 1 (2 semanas): Autenticación + roles, Docker + env example, README ampliado.
- Sprint 2 (2 semanas): API REST básica + OpenAPI, migraciones y seed data, CI básico.
- Sprint 3 (2 semanas): Notificaciones (email), exportes automatizados (CSV/PDF programados).
- Sprint 4 (3 semanas): Tests e instrumentación (logs, monitoring), preparar oferta comercial y pricing.

Estimaciones rápidas (por item):
- Auth (features/auth.py + UI): 2–5 días (medium).
- API REST básica y OpenAPI: 3–7 días (medium).
- Docker + CI: 1–3 días (small).
- Tests iniciales: 2–5 días (medium).
- Notificaciones (email): 2–4 días (medium).

Criterios mínimos para "producto vendible":
- Acceso seguro (auth/roles) y logging de auditoría.
- API pública documentada y estable.
- Proceso de despliegue reproducible (Docker + CI).
- Pruebas automáticas y calidad de código (lint).
- Documentación comercial (pricing, licencia) y legal (privacidad).

Acción inmediata realizada:
Se añade este documento en archivo/analisis_comercial.md para que quede en el repo como punto de partida.

Firma:
GLHF