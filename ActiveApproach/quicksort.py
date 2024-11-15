import random

# Função para implementar o Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Gerar um array de 100 mil números inteiros aleatórios
array = [random.randint(0, 1000000) for _ in range(100000)]

# Ordenar o array usando Quicksort
sorted_array = quicksort(array)

# Verificar os primeiros 10 elementos ordenados (para exemplo)
print(sorted_array[:10])
