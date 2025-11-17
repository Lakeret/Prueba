"""Wrapper para exponer `features.libros` apuntando a la versión 2."""
from .features_libros_Version2 import *

__all__ = [name for name in globals().keys() if not name.startswith("_")]
