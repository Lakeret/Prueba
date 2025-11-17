"""Wrapper para exponer `features.prestamos` apuntando a la versión 2.

Carga el módulo por ruta de archivo para soportar el layout donde las
subcarpetas no tienen `__init__.py`.
"""
import os
import importlib.util

_here = os.path.dirname(__file__)
_candidates = [
	os.path.join(_here, "features_prestamos_Version2", "features_prestamos_Version2.py"),
	os.path.join(_here, "features_prestamos_Version2.py"),
]
_mod_path = next((p for p in _candidates if os.path.isfile(p)), None)
if _mod_path is None:
	raise FileNotFoundError(f"No se encontró el módulo de préstamos en rutas: {_candidates}")
spec = importlib.util.spec_from_file_location("features_prestamos_v2", _mod_path)
_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_mod)

for _name in dir(_mod):
	if not _name.startswith("_"):
		globals()[_name] = getattr(_mod, _name)

__all__ = [name for name in globals().keys() if not name.startswith("_")]
