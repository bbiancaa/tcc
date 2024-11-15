import random

# Função do algoritmo de Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Gerando um array de 100 mil números inteiros aleatórios
array = [random.randint(1, 1000000) for _ in range(100000)]

# Ordenando o array usando Quicksort
sorted_array = quicksort(array)

# Verificando se o array foi ordenado corretamente
print(sorted_array[:10])  # Exibe os primeiros 10 elementos para conferir
