import os
from flask import Flask, render_template, redirect, url_for

# Directorio absoluto del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Crear app Flask usando rutas absolutas
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static')
)

PRODUCTOS = [
    {"id": 1, "nombre": "Tomates", "stock_actual": 5, "pedido_recomendado": 12, "unidad": "kg"},
    {"id": 2, "nombre": "Lechuga", "stock_actual": 3, "pedido_recomendado": 5, "unidad": "uds"},
    {"id": 3, "nombre": "Arroz", "stock_actual": 10, "pedido_recomendado": 8, "unidad": "kg"},
    {"id": 4, "nombre": "Aceite de Oliva", "stock_actual": 2, "pedido_recomendado": 6, "unidad": "L"},
    {"id": 5, "nombre": "Cebolla", "stock_actual": 7, "pedido_recomendado": 10, "unidad": "kg"},
    {"id": 6, "nombre": "Patatas", "stock_actual": 15, "pedido_recomendado": 20, "unidad": "kg"},
    {"id": 7, "nombre": "Pollo", "stock_actual": 4, "pedido_recomendado": 8, "unidad": "kg"},
    {"id": 8, "nombre": "Pescado", "stock_actual": 3, "pedido_recomendado": 7, "unidad": "kg"},
    {"id": 9, "nombre": "Pan", "stock_actual": 20, "pedido_recomendado": 30, "unidad": "uds"},
    {"id": 10, "nombre": "Huevos", "stock_actual": 2, "pedido_recomendado": 5, "unidad": "docenas"},
]

@app.route('/')
def index():
    return render_template('index.html', productos=PRODUCTOS)

@app.route('/confirmar-pedido', methods=['POST'])
def confirmar_pedido():
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
