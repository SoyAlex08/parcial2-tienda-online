"""
Clase Producto para representar un artículo en el catálogo de la tienda
"""

class Producto:
    """Representa un producto de la tienda en línea"""
    
    def __init__(self, id_producto, nombre, precio, categoria, stock, calificacion_promedio):
        self.id = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        self.calificacion_promedio = calificacion_promedio
    
    def __str__(self):
        return f"ID:{self.id} | {self.nombre} | ${self.precio:.2f} | ★{self.calificacion_promedio:.1f} | Stock:{self.stock}"
    
    def __repr__(self):
        return self.__str__()