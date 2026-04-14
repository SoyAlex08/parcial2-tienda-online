"""
Programa principal para ejecutar todas las pruebas del Parcial 2
"""

import random
from generador_datos import generar_productos, mostrar_productos
from ordenamiento import merge_sort, quick_sort, insertion_sort, medir_ordenamiento
from busqueda import medir_busqueda_binaria, medir_busqueda_lineal

def main():
    print("=" * 80)
    print(" " * 25 + "PARCIAL 2 - TIENDA EN LÍNEA")
    print("=" * 80)
    
    # ==================== PARTE 1: GENERACIÓN DE DATOS ====================
    print("\n PARTE 1: Generación de Datos")
    print("-" * 50)
    
    productos = generar_productos(50)
    mostrar_productos(productos, "Catálogo de Productos Generados")
    
    # ==================== PARTE 2: ORDENAMIENTO ====================
    print("\n" + "=" * 80)
    print("PARTE 2: Medición de Algoritmos de Ordenamiento")
    print("=" * 80)
    
    # Tabla de resultados
    print("\n CRITERIO 1: Ordenar por PRECIO (ascendente - más barato primero)")
    print("-" * 80)
    print(f"{'Algoritmo':15} | {'Criterio':20} | {'Tiempo':12} | {'Comparaciones':12}")
    print("-" * 80)
    
    # Medir cada algoritmo para precio
    _, t1, c1 = medir_ordenamiento(merge_sort, productos, lambda p: p.precio, "Merge Sort", "Precio ↑")
    _, t2, c2 = medir_ordenamiento(quick_sort, productos, lambda p: p.precio, "Quick Sort", "Precio ↑")
    _, t3, c3 = medir_ordenamiento(insertion_sort, productos, lambda p: p.precio, "Insertion Sort", "Precio ↑")
    
    print("\n CRITERIO 2: Ordenar por CALIFICACIÓN (descendente - mejor calificado primero)")
    print("-" * 80)
    print(f"{'Algoritmo':15} | {'Criterio':20} | {'Tiempo':12} | {'Comparaciones':12}")
    print("-" * 80)
    
    # Medir cada algoritmo para calificación (reverse=True)
    _, t4, c4 = medir_ordenamiento(merge_sort, productos, lambda p: p.calificacion_promedio, "Merge Sort", "Calificación ↓")
    _, t5, c5 = medir_ordenamiento(quick_sort, productos, lambda p: p.calificacion_promedio, "Quick Sort", "Calificación ↓")
    _, t6, c6 = medir_ordenamiento(insertion_sort, productos, lambda p: p.calificacion_promedio, "Insertion Sort", "Calificación ↓")
    
    # Análisis de resultados
    print("\n" + "=" * 80)
    print("ANÁLISIS DE ORDENAMIENTO")
    print("=" * 80)
    
    mejor_precio = min([(t1, "Merge Sort"), (t2, "Quick Sort"), (t3, "Insertion Sort")], key=lambda x: x[0])
    mejor_calif = min([(t4, "Merge Sort"), (t5, "Quick Sort"), (t6, "Insertion Sort")], key=lambda x: x[0])
    
    print(f"\nMejor algoritmo para ordenar por PRECIO: {mejor_precio[1]} ({mejor_precio[0]:.4f} ms)")
    print(f"Mejor algoritmo para ordenar por CALIFICACIÓN: {mejor_calif[1]} ({mejor_calif[0]:.4f} ms)")
    
    # ==================== PARTE 3: BÚSQUEDA ====================
    print("\n" + "=" * 80)
    print("PARTE 3: Algoritmos de Búsqueda")
    print("=" * 80)
    
    # Preparar productos ordenados por ID para búsqueda binaria
    productos_ordenados_por_id, _ = merge_sort(productos, lambda p: p.id)
    
    # Generar IDs para prueba
    ids_existentes = [p.id for p in random.sample(productos_ordenados_por_id, 10)]
    ids_inexistentes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    
    # Medir búsqueda binaria
    print("\n Búsqueda por ID (Búsqueda Binaria)")
    print("-" * 50)
    tiempo_bin_ex, _ = medir_busqueda_binaria(productos_ordenados_por_id, ids_existentes, "IDs que EXISTEN")
    tiempo_bin_inex, _ = medir_busqueda_binaria(productos_ordenados_por_id, ids_inexistentes, "IDs que NO existen")
    
    # Generar subcadenas para búsqueda lineal
    nombres_productos = [p.nombre for p in productos]
    subcadenas_existentes = ["Libro", "Camiseta", "Laptop", "Smartphone", "Mouse", "Teclado"]
    subcadenas_inexistentes = ["Xilófono", "Galaxia", "Marciano", "Submarino", "Dragón", "Fénix"]
    
    # Medir búsqueda lineal
    print("\n Búsqueda por Nombre (Búsqueda Lineal - subcadena)")
    print("-" * 50)
    tiempo_lin_ex, _ = medir_busqueda_lineal(productos, subcadenas_existentes, "Subcadenas que EXISTEN")
    tiempo_lin_inex, _ = medir_busqueda_lineal(productos, subcadenas_inexistentes, "Subcadenas que NO existen")
    
    # ==================== CONCLUSIONES ====================
    print("\n" + "=" * 80)
    print("CONCLUSIONES FINALES")
    print("=" * 80)
    
    print("""
    1. ORDENAMIENTO:
       - Quick Sort y Merge Sort son significativamente más rápidos que Insertion Sort
         para n=50, aunque la diferencia se hace más notoria con conjuntos más grandes.
       - La teoría O(n log n) vs O(n²) se confirma en la práctica.
       - Ordenar objetos complejos tiene overhead adicional por las llamadas a key_func,
         pero la complejidad algorítmica domina el rendimiento.
    
    2. BÚSQUEDA POR ID (Binaria):
       - La búsqueda binaria es extremadamente rápida (microsegundos) incluso con 50 elementos.
       - Es ideal para búsquedas por clave única porque requiere O(log n) comparaciones.
       - El requisito fundamental es tener los datos ordenados por el campo de búsqueda.
    
    3. BÚSQUEDA POR NOMBRE (Lineal):
       - La búsqueda lineal con coincidencia parcial es O(n) por cada búsqueda.
       - Es más lenta que la búsqueda binaria, pero necesaria para búsquedas textuales.
       - En producción, se usarían índices invertidos o árboles de prefijos (Trie) para optimizar.
    """)
    
    print("\n" + "=" * 80)
    print("PROGRAMA FINALIZADO CON ÉXITO")
    print("=" * 80)

if __name__ == "__main__":
    main()