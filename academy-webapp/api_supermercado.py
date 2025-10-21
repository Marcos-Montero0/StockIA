from fastapi import FastAPI, Request
import sqlite3

app = FastAPI(title="API Supermercado")

@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la API del supermercado 🛒"}

@app.get("/productos")
def obtener_productos():
    conn = sqlite3.connect("supermercado.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, precio, stock FROM productos")
    filas = cursor.fetchall()
    conn.close()

    productos = [
        {"nombre": fila[0], "precio": fila[1], "stock": fila[2]}
        for fila in filas
    ]
    return {"productos": productos}


@app.post("/agregar_producto")
def agregar_producto(datos: dict):
    nombre = datos.get("nombre")
    precio = datos.get("precio")
    stock = datos.get("stock")

    if not all([nombre, precio is not None, stock is not None]):
        return {"error": "Faltan datos: nombre, precio o stock."}

    conn = sqlite3.connect("supermercado.db")
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
            (nombre, precio, stock)
        )
        conn.commit()
        return {"mensaje": f" Producto '{nombre}' agregado correctamente."}
    except sqlite3.IntegrityError:
        return {"error": f" El producto '{nombre}' ya existe."}
    finally:
        conn.close()


@app.delete("/eliminar_producto")
def eliminar_producto(datos: dict):
    nombre = datos.get("nombre")

    if not nombre:
        return {"error": "Falta el campo 'nombre'."}

    conn = sqlite3.connect("supermercado.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM productos WHERE nombre = ?", (nombre,))
    conn.commit()
    filas_afectadas = cursor.rowcount
    conn.close()

    if filas_afectadas == 0:
        return {"mensaje": f" No se encontró el producto '{nombre}'."}
    else:
        return {"mensaje": f" Producto '{nombre}' eliminado correctamente."}


@app.put("/actualizar_producto")
def actualizar_producto(datos: dict):
    nombre = datos.get("nombre")
    nuevo_precio = datos.get("precio")
    nuevo_stock = datos.get("stock")

    if not nombre:
        return {"error": "Debes indicar el nombre del producto."}

    conn = sqlite3.connect("supermercado.db")
    cursor = conn.cursor()

    # Construir la consulta dinámicamente (solo actualiza lo que venga en el JSON)
    campos = []
    valores = []
    if nuevo_precio is not None:
        campos.append("precio = ?")
        valores.append(nuevo_precio)
    if nuevo_stock is not None:
        campos.append("stock = ?")
        valores.append(nuevo_stock)

    # Si no se pasa ni precio ni stock, no hay nada que actualizar
    if not campos:
        return {"error": "Debes indicar al menos 'precio' o 'stock' para actualizar."}

    valores.append(nombre)
    consulta = f"UPDATE productos SET {', '.join(campos)} WHERE nombre = ?"
    cursor.execute(consulta, tuple(valores))
    conn.commit()
    filas_afectadas = cursor.rowcount
    conn.close()

    if filas_afectadas == 0:
        return {"mensaje": f" No se encontró el producto '{nombre}'."}
    else:
        return {"mensaje": f" Producto '{nombre}' actualizado correctamente."}