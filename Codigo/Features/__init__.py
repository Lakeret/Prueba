"""Paquete `features` — expone los módulos con los nombres que usa la interfaz.

Este archivo mapea los módulos reales (versionados) a nombres sencillos
como `features.libros`, `features.prestamos`, `features.reportes`.
"""
from . import libros
from . import prestamos
from . import reportes

__all__ = ["libros", "prestamos", "reportes"]
