def quicksort(arr):
    """
    Implementa el algoritmo de ordenamiento Quicksort.
    
    Parámetros:
    arr (list): Lista de elementos a ordenar.
    
    Retorna:
    list: Lista ordenada.
    """
    if len(arr) <= 1:
        return arr  # Caso base: listas de 0 o 1 elemento están ordenadas
    
    pivot = arr[0]  # Selecciona el primer elemento como pivote
    left = [x for x in arr[1:] if x < pivot]  # Elementos menores que el pivote
    right = [x for x in arr[1:] if x >= pivot]  # Elementos mayores o iguales que el pivote
    
    # Llamadas recursivas
    return quicksort(left) + [pivot] + quicksort(right)

# Pruebas con diferentes listas de entrada
test_lists = [
    [34, 7, 23, 32, 5, 62],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [5, 3, 8, 3, 2, 7, 3, 5],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [42],
    []
]

for i, test_list in enumerate(test_lists):
    sorted_list = quicksort(test_list)
    print(f"Prueba {i+1}:")
    print(f"Array original: {test_list}")
    print(f"Array ordenado: {sorted_list}")
    print()
