"""
Algoritmos de ordenamiento para objetos Producto
"""

import time
from producto import Producto

# ==================== 1. MERGE SORT ====================

def merge_sort(productos, key_func, reverse=False):
    """
    Merge Sort para ordenar productos según una clave
    
    Args:
        productos: Lista de productos a ordenar
        key_func: Función que extrae el valor a comparar (ej: lambda p: p.precio)
        reverse: Si es True, orden descendente
    
    Returns:
        Lista ordenada y número de comparaciones
    """
    if len(productos) <= 1:
        return productos, 0
    
    medio = len(productos) // 2
    izquierda, comp_izq = merge_sort(productos[:medio], key_func, reverse)
    derecha, comp_der = merge_sort(productos[medio:], key_func, reverse)
    
    resultado, comp_merge = merge(izquierda, derecha, key_func, reverse)
    
    return resultado, comp_izq + comp_der + comp_merge

def merge(izquierda, derecha, key_func, reverse):
    """Función auxiliar para fusionar dos listas ordenadas"""
    resultado = []
    i = j = 0
    comparaciones = 0
    
    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1
        valor_izq = key_func(izquierda[i])
        valor_der = key_func(derecha[j])
        
        if reverse:
            # Orden descendente
            if valor_izq >= valor_der:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1
        else:
            # Orden ascendente
            if valor_izq <= valor_der:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1
    
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado, comparaciones

# ==================== 2. QUICK SORT ====================

def quick_sort(productos, key_func, reverse=False):
    """
    Quick Sort para ordenar productos según una clave
    """
    if len(productos) <= 1:
        return productos, 0
    
    pivote = productos[len(productos) // 2]
    valor_pivote = key_func(pivote)
    
    menores = []
    iguales = []
    mayores = []
    comparaciones = 0
    
    for p in productos:
        comparaciones += 1
        valor_actual = key_func(p)
        
        if reverse:
            # Orden descendente
            if valor_actual > valor_pivote:
                menores.append(p)
            elif valor_actual < valor_pivote:
                mayores.append(p)
            else:
                iguales.append(p)
        else:
            # Orden ascendente
            if valor_actual < valor_pivote:
                menores.append(p)
            elif valor_actual > valor_pivote:
                mayores.append(p)
            else:
                iguales.append(p)
    
    menores_ord, comp_men = quick_sort(menores, key_func, reverse)
    mayores_ord, comp_may = quick_sort(mayores, key_func, reverse)
    
    return menores_ord + iguales + mayores_ord, comparaciones + comp_men + comp_may

# ==================== 3. INSERTION SORT ====================

def insertion_sort(productos, key_func, reverse=False):
    """
    Insertion Sort para ordenar productos según una clave
    """
    if not productos:
        return productos, 0
    
    productos = productos.copy()
    comparaciones = 0
    
    for i in range(1, len(productos)):
        actual = productos[i]
        valor_actual = key_func(actual)
        j = i - 1
        
        while j >= 0:
            comparaciones += 1
            valor_j = key_func(productos[j])
            
            if reverse:
                condicion = valor_j < valor_actual
            else:
                condicion = valor_j > valor_actual
            
            if condicion:
                productos[j + 1] = productos[j]
                j -= 1
            else:
                break
        
        productos[j + 1] = actual
    
    return productos, comparaciones

# ==================== FUNCIÓN DE MEDICIÓN ====================

def medir_ordenamiento(algoritmo, productos, key_func, nombre_algoritmo, criterio):
    """
    Mide el tiempo de ejecución de un algoritmo de ordenamiento
    """
    # Crear una copia para no modificar el original
    copia = productos.copy()
    
    inicio = time.time()
    ordenados, comparaciones = algoritmo(copia, key_func)
    fin = time.time()
    
    tiempo_ms = (fin - inicio) * 1000
    
    print(f"{nombre_algoritmo:15} | {criterio:20} | {tiempo_ms:8.4f} ms | {comparaciones:6} comps")
    
    return ordenados, tiempo_ms, comparaciones

# Prueba rápida
if __name__ == "__main__":
    from generador_datos import generar_productos
    
    productos = generar_productos(20)
    
    print("\n--- Prueba de ordenamiento ---")
    print("Algoritmo        | Criterio             | Tiempo      | Comparaciones")
    print("-" * 70)
    
    # Probar por precio (ascendente)
    medir_ordenamiento(merge_sort, productos, lambda p: p.precio, "Merge Sort", "Precio ↑")
    medir_ordenamiento(quick_sort, productos, lambda p: p.precio, "Quick Sort", "Precio ↑")
    medir_ordenamiento(insertion_sort, productos, lambda p: p.precio, "Insertion Sort", "Precio ↑")
    
    # Probar por calificación (descendente)
    medir_ordenamiento(merge_sort, productos, lambda p: p.calificacion_promedio, "Merge Sort", "Calificación ↓")
    medir_ordenamiento(quick_sort, productos, lambda p: p.calificacion_promedio, "Quick Sort", "Calificación ↓")
    medir_ordenamiento(insertion_sort, productos, lambda p: p.calificacion_promedio, "Insertion Sort", "Calificación ↓")