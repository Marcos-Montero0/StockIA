import sqlite3

# Conectamos a la base de datos existente
conn = sqlite3.connect("stock.db")
cursor = conn.cursor()

# Diccionario con tus productos
productos = {
    "hamburguesa": {"stock_actual": 5, "stock_deseado": 30},
    "pan": {"stock_actual": 12, "stock_deseado": 15},
    "patata": {"stock_actual": 11, "stock_deseado": 9},
    "chocolate": {"stock_actual": 25, "stock_deseado": 50},
    "arroz": {"stock_actual": 9, "stock_deseado": 20}
}

# Insertar productos en la tabla
for nombre, datos in productos.items():
    cursor.execute("""
        INSERT OR REPLACE INTO productos (nombre, stock_actual, stock_deseado)
        VALUES (?, ?, ?)
    """, (nombre, datos["stock_actual"], datos["stock_deseado"]))

# Guardar los cambios
conn.commit()
conn.close()

print(" Productos insertados correctamente en la base de datos.")
