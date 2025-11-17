from db import execute
from datetime import datetime

def generar_reporte(tipo_reporte, descripcion, resultado_texto, usuario_genero):
    fecha = datetime.utcnow().date()
    return execute(
        "INSERT INTO reportes (tipo_reporte, fecha_generacion, descripcion, resultado, usuario_genero) VALUES (%s,%s,%s,%s,%s)",
        (tipo_reporte, fecha, descripcion, resultado_texto, usuario_genero)
    )