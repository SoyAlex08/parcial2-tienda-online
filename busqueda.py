"""
Algoritmos de búsqueda para productos
"""

import time
import random

def busqueda_binaria_por_id(productos, id_buscado):
    """
    Búsqueda binaria para encontrar producto por ID
    
    Args:
        productos: Lista ordenada por ID
        id_buscado: ID a buscar
    
    Returns:
        (producto_encontrado, índice, número_de_comparaciones)
    """
    izquierda = 0
    derecha = len(productos) - 1
    comparaciones = 0
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        comparaciones += 1
        
        if productos[medio].id == id_buscado:
            return productos[medio], medio, comparaciones
        elif productos[medio].id < id_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
        comparaciones += 1
    
    return None, -1, comparaciones

def busqueda_lineal_por_nombre(productos, subcadena):
    """
    Búsqueda lineal para encontrar productos cuyo nombre contiene una subcadena
    
    Args:
        productos: Lista de productos
        subcadena: Texto a buscar en el nombre
    
    Returns:
        (lista_de_resultados, número_de_comparaciones)
    """
    resultados = []
    comparaciones = 0
    
    for producto in productos:
        comparaciones += 1
        if subcadena.lower() in producto.nombre.lower():
            resultados.append(producto)
    
    return resultados, comparaciones

def medir_busqueda_binaria(productos, ids_a_buscar, descripcion=""):
    """
    Mide el rendimiento de la búsqueda binaria para múltiples IDs
    """
    tiempos = []
    total_comparaciones = 0
    exitosos = 0
    
    print(f"\n--- Búsqueda Binaria: {descripcion} ---")
    
    for id_buscado in ids_a_buscar:
        inicio = time.time()
        producto, pos, comps = busqueda_binaria_por_id(productos, id_buscado)
        fin = time.time()
        
        tiempo_us = (fin - inicio) * 1000000  # microsegundos
        tiempos.append(tiempo_us)
        total_comparaciones += comps
        
        if producto:
            exitosos += 1
            # print(f"  ✓ ID {id_buscado} encontrado: {producto.nombre} (pos {pos})")
        else:
            pass  # print(f"  ✗ ID {id_buscado} no encontrado")
    
    tiempo_promedio = sum(tiempos) / len(tiempos)
    
    print(f"Resultados: {exitosos}/{len(ids_a_buscar)} encontrados")
    print(f"Tiempo promedio: {tiempo_promedio:.2f} µs")
    print(f"Comparaciones promedio: {total_comparaciones/len(ids_a_buscar):.1f}")
    
    return tiempo_promedio, total_comparaciones

def medir_busqueda_lineal(productos, subcadenas_a_buscar, descripcion=""):
    """
    Mide el rendimiento de la búsqueda lineal para múltiples subcadenas
    """
    tiempos = []
    total_comparaciones = 0
    exitosos = 0
    
    print(f"\n--- Búsqueda Lineal: {descripcion} ---")
    
    for subcadena in subcadenas_a_buscar:
        inicio = time.time()
        resultados, comps = busqueda_lineal_por_nombre(productos, subcadena)
        fin = time.time()
        
        tiempo_us = (fin - inicio) * 1000000
        tiempos.append(tiempo_us)
        total_comparaciones += comps
        
        if resultados:
            exitosos += 1
            # print(f"  ✓ '{subcadena}' -> {len(resultados)} resultados")
        else:
            pass  # print(f"  ✗ '{subcadena}' -> 0 resultados")
    
    tiempo_promedio = sum(tiempos) / len(tiempos)
    
    print(f"Resultados: {exitosos}/{len(subcadenas_a_buscar)} búsquedas con resultados")
    print(f"Tiempo promedio: {tiempo_promedio:.2f} µs")
    print(f"Comparaciones promedio: {total_comparaciones/len(subcadenas_a_buscar):.1f}")
    
    return tiempo_promedio, total_comparaciones

# Prueba rápida
if __name__ == "__main__":
    from generador_datos import generar_productos
    from ordenamiento import merge_sort
    
    # Generar productos y ordenar por ID
    productos = generar_productos(50)
    productos_ordenados, _ = merge_sort(productos, lambda p: p.id)
    
    # Prueba de búsqueda binaria
    ids_existentes = [p.id for p in productos_ordenados[:10]]
    ids_inexistentes = [999, 888, 777, 666, 555, 444, 333, 222, 111, 0]
    
    medir_busqueda_binaria(productos_ordenados, ids_existentes, "IDs que EXISTEN")
    medir_busqueda_binaria(productos_ordenados, ids_inexistentes, "IDs que NO existen")
    
    # Prueba de búsqueda lineal
    subcadenas_existentes = ["Libro", "Camiseta", "Laptop", "Smartphone"]
    subcadenas_inexistentes = ["Xilófono", "Galaxia", "Marciano", "Submarino"]
    
    medir_busqueda_lineal(productos, subcadenas_existentes, "Subcadenas que EXISTEN")
    medir_busqueda_lineal(productos, subcadenas_inexistentes, "Subcadenas que NO existen")