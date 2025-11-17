from db import fetchall_dict, fetchone_dict

def total_libros():
    row = fetchone_dict("SELECT COUNT(*) AS total FROM libros")
    return row.get('total', 0) if row else 0

def libros_por_genero():
    return fetchall_dict("SELECT genero, COUNT(*) AS cantidad FROM libros GROUP BY genero ORDER BY cantidad DESC")

def prestamos_activos_count():
    row = fetchone_dict("SELECT COUNT(*) AS total FROM prestamos WHERE devuelto = '0'")
    return row.get('total', 0) if row else 0

def top_usuarios_por_prestamos(limit=5):
    return fetchall_dict(
        "SELECT u.nombre, COUNT(*) AS cantidad FROM prestamos p JOIN usuarios u ON p.id_usuario = u.id_usuario GROUP BY u.id_usuario ORDER BY cantidad DESC LIMIT %s",
        (limit,)
    )

# Helpers para consumo por la interfaz
def resumen_estadisticas():
    return {
        'total_libros': total_libros(),
        'prestamos_activos': prestamos_activos_count(),
        'libros_por_genero': libros_por_genero(),
        'top_usuarios': top_usuarios_por_prestamos(5)
    }