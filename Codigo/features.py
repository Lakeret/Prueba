"""Shim para compatibilidad: expone el paquete real `Features` como `features`.

Esto permite que código que hace `import features` funcione sin renombrar
la carpeta `Features` en Windows/otros entornos.
"""
import importlib
_real = importlib.import_module('Features')

for _name in ('libros', 'prestamos', 'reportes'):
    if hasattr(_real, _name):
        globals()[_name] = getattr(_real, _name)

__all__ = [name for name in globals().keys() if not name.startswith("_")]
