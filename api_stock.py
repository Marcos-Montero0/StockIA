from fastapi import FastAPI, Request
import sqlite3

app = FastAPI(title="API Stock")

@app.get("/pedido")
def obtener_pedido():
    conn = sqlite3.connect("stock.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, stock_actual, stock_deseado FROM productos")
    filas = cursor.fetchall()
    conn.close()

    pedido = []
    for nombre, stock_actual, stock_deseado in filas:
        cantidad_pedir = stock_deseado - stock_actual
        if cantidad_pedir > 0:
            pedido.append({
                "nombre": nombre,
                "stock_pedir": cantidad_pedir
            })

    return {"pedido": pedido}



@app.post("/actualizar_stock")
def actualizar_stock(datos: dict):
    nombre = datos.get("nombre")
    nuevo_stock = datos.get("stock_actual")

    #if not nombre or nuevo_stock is None:
    #   raise HTTPException(status_code=400, detail="Debes indicar 'nombre' y 'stock_actual'.")

    conn = sqlite3.connect("stock.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE productos SET stock_actual = ? WHERE nombre = ?", (nuevo_stock, nombre))
    conn.commit()
    filas_afectadas = cursor.rowcount
    conn.close()

    if filas_afectadas == 0:
        return {"mensaje": f"No se encontró el producto '{nombre}'."}
    else:
        return {"mensaje": f"Stock de '{nombre}' actualizado correctamente a {nuevo_stock}."}