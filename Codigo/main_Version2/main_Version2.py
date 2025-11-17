import tkinter as tk
from tkinter import ttk, messagebox
from features import libros, prestamos, reportes

def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Sistema Biblioteca (modular)")
    ventana.geometry("1000x600")

    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=8, fill="x")

    def mostrar_todos():
        for r in tabla.get_children(): tabla.delete(r)
        datos = libros.seleccionar_todos_los_libros()
        for l in datos:
            tabla.insert("", "end", values=(
                l['id_libro'], l['titulo'], l.get('autor',''), l.get('genero',''),
                l.get('publicacion',''), l.get('cantidad_disponible',''), l.get('calificacion',''),
                l.get('prestamos','') or ''
            ))

    def ventana_agregar():
        win = tk.Toplevel(ventana)
        win.title("Agregar Libro")
        entradas = {}
        campos = [("titulo","Título"), ("autor","Autor"), ("genero","Género"), ("publicacion","Publicación (YYYY-MM-DD)"), ("cantidad","Cantidad"), ("calificacion","Calificación")]
        for key, label in campos:
            tk.Label(win, text=label).pack(anchor="w")
            e = tk.Entry(win)
            e.pack(fill="x")
            entradas[key] = e
        def guardar():
            try:
                libros.agregar_libro(
                    entradas["titulo"].get().strip(),
                    entradas["autor"].get().strip(),
                    entradas["genero"].get().strip(),
                    entradas["publicacion"].get().strip(),
                    int(entradas["cantidad"].get().strip()),
                    int(entradas["calificacion"].get().strip())
                )
                messagebox.showinfo("OK","Libro agregado")
                win.destroy()
                mostrar_todos()
            except Exception as ex:
                messagebox.showerror("Error", str(ex))
        tk.Button(win, text="Guardar", command=guardar).pack(pady=8)

    def ventana_prestar():
        win = tk.Toplevel(ventana)
        tk.Label(win, text="ID Libro").pack()
        id_lib = tk.Entry(win); id_lib.pack()
        tk.Label(win, text="ID Usuario").pack()
        id_usr = tk.Entry(win); id_usr.pack()
        tk.Label(win, text="Días (por defecto 14)").pack()
        dias = tk.Entry(win); dias.insert(0,"14"); dias.pack()
        def prestar_action():
            try:
                prestamos.prestar_libro(int(id_lib.get()), int(id_usr.get()), int(dias.get()))
                messagebox.showinfo("OK","Préstamo registrado")
                win.destroy()
                mostrar_todos()
            except Exception as ex:
                messagebox.showerror("Error", str(ex))
        tk.Button(win, text="Prestar", command=prestar_action).pack(pady=6)

    def ventana_devolver():
        win = tk.Toplevel(ventana)
        tk.Label(win, text="ID Préstamo").pack()
        idp = tk.Entry(win); idp.pack()
        def devolver_action():
            try:
                prestamos.devolver_libro(int(idp.get()))
                messagebox.showinfo("OK","Devolución registrada")
                win.destroy()
                mostrar_todos()
            except Exception as ex:
                messagebox.showerror("Error", str(ex))
        tk.Button(win, text="Devolver", command=devolver_action).pack(pady=6)

    botones = [
        ("Mostrar Todos", mostrar_todos),
        ("Agregar Libro", ventana_agregar),
        ("Prestar Libro", ventana_prestar),
        ("Devolver Libro", ventana_devolver),
    ]
    for (txt, cmd) in botones:
        tk.Button(frame_botones, text=txt, command=cmd, width=16).pack(side="left", padx=4)

    columnas = ("ID","Título","Autor","Género","Publicación","Cantidad","Calificación","Préstamos")
    global tabla
    tabla = ttk.Treeview(ventana, columns=columnas, show="headings")
    for col in columnas:
        tabla.heading(col, text=col)
        if col == "Préstamos":
            tabla.column(col, width=350)
    tabla.pack(fill="both", expand=True, pady=10)

    # Mostrar al inicio
    mostrar_todos()

    ventana.mainloop()

if __name__ == "__main__":
    crear_interfaz()