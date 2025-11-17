"""Shim para exponer la implementación de base de datos usada por los módulos.

Carga el archivo `db_Version2/db_Version2.py` por ruta y exporta sus símbolos
como si fuesen parte del módulo `db` para mantener compatibilidad con
importaciones existentes (`from db import fetchall_dict`, etc.).
"""
import os
import importlib.util

_here = os.path.dirname(__file__)
_root = os.path.abspath(os.path.join(_here, os.pardir))
_path = os.path.join(_root, 'db_Version2', 'db_Version2.py')

spec = importlib.util.spec_from_file_location('db_v2_impl', _path)
_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_mod)

for _name in dir(_mod):
    if not _name.startswith('_'):
        globals()[_name] = getattr(_mod, _name)

__all__ = [name for name in globals().keys() if not name.startswith('_')]
