```markdown
# Biblioteca — estructura modular

Proyecto de ejemplo que organiza cada funcionalidad en un archivo Python dentro del paquete `features/`.

Archivos principales:
- `main.py`: Interfaz gráfica (Tkinter) que importa funcionalidades.
- `config.py`: Configuración de base de datos (placeholders).
- `db.py`: Conexión y utilidades SQL.
- `features/`: Paquete con archivos por funcionalidad (libros, prestamos, reportes).

Pasos para usar:
1. Crear entorno virtual:
   - Linux/Mac: `python -m venv venv && source venv/bin/activate`
   - Windows: `python -m venv venv && venv\Scripts\activate`
2. Instalar dependencias:
   - `pip install mysql-connector-python`
3. Configurar credenciales en `config.py`.
4. Ejecutar:
   - `python main.py`

Subir a GitHub (ejemplo de comandos):
```
git init
git add .
git commit -m "Initial modular biblioteca app"
git branch -M main
git remote add origin https://github.com/Lakeret/EXAMEN-.git
git push -u origin main
```
```