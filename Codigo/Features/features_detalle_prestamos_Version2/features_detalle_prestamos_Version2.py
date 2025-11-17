from db import fetchall_dict

def obtener_prestamos_por_libro(id_libro):
    return fetchall_dict(
        """
        SELECT p.id_prestamo, u.nombre AS usuario, p.fecha_prestamo, p.fecha_devolucion, p.devuelto
        FROM prestamos p
        LEFT JOIN usuarios u ON p.id_usuario = u.id_usuario
        WHERE p.id_libro = %s
        ORDER BY p.fecha_prestamo DESC
        """,
        (id_libro,)
    )