from db import fetchall_dict, conectar
from datetime import datetime, timedelta

def prestar_libro(id_libro, id_usuario, dias=14):
    con = conectar()
    try:
        cur = con.cursor(dictionary=True)
        cur.execute("SELECT cantidad_disponible FROM libros WHERE id_libro = %s FOR UPDATE", (id_libro,))
        fila = cur.fetchone()
        if not fila:
            raise ValueError("El libro no existe.")
        if fila['cantidad_disponible'] <= 0:
            raise ValueError("No hay unidades disponibles.")
        fecha_prestamo = datetime.utcnow().date()
        fecha_devolucion = fecha_prestamo + timedelta(days=int(dias))
        cur.execute("INSERT INTO prestamos (id_libro, id_usuario, fecha_prestamo, fecha_devolucion, devuelto) VALUES (%s,%s,%s,%s,%s)",
                    (id_libro, id_usuario, fecha_prestamo, fecha_devolucion, '0'))
        cur.execute("UPDATE libros SET cantidad_disponible = cantidad_disponible - 1 WHERE id_libro = %s", (id_libro,))
        con.commit()
        return cur.lastrowid
    except Exception:
        con.rollback()
        raise
    finally:
        cur.close()
        con.close()

def devolver_libro(id_prestamo):
    con = conectar()
    try:
        cur = con.cursor(dictionary=True)
        cur.execute("SELECT id_libro, devuelto FROM prestamos WHERE id_prestamo = %s", (id_prestamo,))
        p = cur.fetchone()
        if not p:
            raise ValueError("Préstamo no encontrado.")
        if p['devuelto'] == '1':
            raise ValueError("Préstamo ya devuelto.")
        fecha = datetime.utcnow().date()
        cur.execute("UPDATE prestamos SET devuelto = '1', fecha_devolucion = %s WHERE id_prestamo = %s", (fecha, id_prestamo))
        cur.execute("UPDATE libros SET cantidad_disponible = cantidad_disponible + 1 WHERE id_libro = %s", (p['id_libro'],))
        con.commit()
        return True
    except Exception:
        con.rollback()
        raise
    finally:
        cur.close()
        con.close()

def obtener_prestamos_vencidos():
    return fetchall_dict("""
        SELECT p.id_prestamo, u.nombre AS usuario, l.titulo AS libro, p.fecha_prestamo, p.fecha_devolucion
        FROM prestamos p
        JOIN usuarios u ON p.id_usuario = u.id_usuario
        JOIN libros l ON p.id_libro = l.id_libro
        WHERE p.devuelto = '0' AND p.fecha_devolucion < CURDATE()
        ORDER BY p.fecha_devolucion
    """)