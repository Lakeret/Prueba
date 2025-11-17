"""Shim para exponer configuración como `config`.

Carga `config_Version2/config_Version2.py` y exporta su símbolos con el nombre
`config` para que importaciones como `from config import DB_CONFIG` funcionen.
"""
import os
import importlib.util

_here = os.path.dirname(__file__)
_root = os.path.abspath(os.path.join(_here, os.pardir))
_path = os.path.join(_root, 'config_Version2', 'config_Version2.py')

spec = importlib.util.spec_from_file_location('config_v2_impl', _path)
_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_mod)

for _name in dir(_mod):
    if not _name.startswith('_'):
        globals()[_name] = getattr(_mod, _name)

__all__ = [name for name in globals().keys() if not name.startswith('_')]
