import sqlite3

# Conectar o crear la base de datos local
conn = sqlite3.connect("stock.db")

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear la tabla 'productos' si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    nombre TEXT PRIMARY KEY,
    stock_actual INTEGER,
    stock_deseado INTEGER
)
""")

# Guardar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print(" Tabla 'productos' creada correctamente en supermercado.db")
