import csv
from features.libros import seleccionar_todos_los_libros

def exportar_libros_csv(path):
    libros = seleccionar_todos_los_libros()
    # campos: id,titulo,autor,genero,publicacion,cantidad,calificacion,prestamos
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id_libro','titulo','autor','genero','publicacion','cantidad_disponible','calificacion','prestamos'])
        for l in libros:
            writer.writerow([
                l.get('id_libro',''),
                l.get('titulo',''),
                l.get('autor',''),
                l.get('genero',''),
                l.get('publicacion',''),
                l.get('cantidad_disponible',''),
                l.get('calificacion',''),
                l.get('prestamos','') or ''
            ])
    return path