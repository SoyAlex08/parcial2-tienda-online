"""
Generador de datos aleatorios para productos
"""

import random
from producto import Producto

# Listas predefinidas para generar datos realistas
NOMBRES_PRODUCTOS = [
    "Laptop", "Smartphone", "Tablet", "Auriculares", "Teclado", "Mouse", "Monitor", "Impresora",
    "Camiseta", "Pantalón", "Zapatos", "Gorra", "Bufanda", "Chaqueta", "Vestido", "Jeans",
    "Libro Python", "Libro Java", "Libro Robótica", "Diccionario", "Enciclopedia", "Novela",
    "Lámpara", "Sofá", "Mesa", "Silla", "Estante", "Cama", "Cortinas", "Almohadas"
]

CATEGORIAS = ["Electrónica", "Ropa", "Libros", "Hogar"]

def generar_productos(cantidad=50):
    """
    Genera una lista de productos con datos aleatorios
    
    Args:
        cantidad: Número de productos a generar
    
    Returns:
        Lista de objetos Producto
    """
    productos = []
    
    for i in range(1, cantidad + 1):
        # Generar datos aleatorios pero coherentes
        nombre = random.choice(NOMBRES_PRODUCTOS) + " " + str(random.randint(1, 100))
        precio = round(random.uniform(5.99, 999.99), 2)
        categoria = random.choice(CATEGORIAS)
        stock = random.randint(0, 500)
        calificacion = round(random.uniform(1.0, 5.0), 1)
        
        producto = Producto(i, nombre, precio, categoria, stock, calificacion)
        productos.append(producto)
    
    return productos

def mostrar_productos(productos, titulo="Lista de Productos"):
    """Muestra una lista de productos en formato tabla"""
    print(f"\n--- {titulo} ---")
    print("-" * 80)
    for p in productos:
        print(p)
    print("-" * 80)
    print(f"Total: {len(productos)} productos\n")

# Prueba rápida
if __name__ == "__main__":
    productos = generar_productos(10)
    mostrar_productos(productos, "Muestra de Productos Generados")