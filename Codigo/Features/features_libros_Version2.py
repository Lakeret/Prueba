from db import fetchall_dict, fetchone_dict, execute
from datetime import datetime

def seleccionar_todos_los_libros():
    return fetchall_dict("""
        SELECT l.id_libro, l.titulo, l.autor, l.genero, l.publicacion, l.cantidad_disponible, l.calificacion,
               GROUP_CONCAT(CONCAT(u.nombre, ' (', DATE_FORMAT(p.fecha_prestamo, '%Y-%m-%d'), ' → ', DATE_FORMAT(p.fecha_devolucion, '%Y-%m-%d'), ')') SEPARATOR '; ') AS prestamos
        FROM libros l
        LEFT JOIN prestamos p ON l.id_libro = p.id_libro
        LEFT JOIN usuarios u ON p.id_usuario = u.id_usuario
        GROUP BY l.id_libro
        ORDER BY l.titulo
    """)

def consultar_libros_mas_populares(limit=10):
    return fetchall_dict("""
        SELECT l.id_libro, l.titulo, l.calificacion,
               GROUP_CONCAT(CONCAT(u.nombre, ' (', DATE_FORMAT(p.fecha_prestamo, '%Y-%m-%d'), ' → ', DATE_FORMAT(p.fecha_devolucion, '%Y-%m-%d'), ')') SEPARATOR '; ') AS prestamos
        FROM libros l
        LEFT JOIN prestamos p ON l.id_libro = p.id_libro
        LEFT JOIN usuarios u ON p.id_usuario = u.id_usuario
        WHERE l.calificacion >= 4
        GROUP BY l.id_libro
        ORDER BY l.calificacion DESC, l.titulo
        LIMIT %s
    """, (limit,))

def agregar_libro(titulo, autor, genero, publicacion, cantidad_disponible, calificacion):
    if publicacion:
        # valida formato YYYY-MM-DD
        datetime.strptime(publicacion, "%Y-%m-%d")
    return execute(
        "INSERT INTO libros (titulo, autor, genero, publicacion, cantidad_disponible, calificacion) VALUES (%s,%s,%s,%s,%s,%s)",
        (titulo, autor, genero or None, publicacion or None, int(cantidad_disponible), int(calificacion))
    )

def eliminar_libro(id_libro):
    return execute("DELETE FROM libros WHERE id_libro = %s", (id_libro,))

def buscar_libro_por_titulo_exacto(titulo):
    return fetchone_dict("SELECT * FROM libros WHERE LOWER(titulo) = LOWER(%s) LIMIT 1", (titulo,))

def buscar_libros_por_titulo_parcial(termino):
    like = f"%{termino}%"
    return fetchall_dict("SELECT * FROM libros WHERE LOWER(titulo) LIKE LOWER(%s) ORDER BY titulo", (like,))