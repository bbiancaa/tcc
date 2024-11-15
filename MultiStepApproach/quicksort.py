import random

# Função de particionamento
def partition(arr, low, high):
    pivot = arr[high]  # Escolhe o último elemento como pivô
    i = low - 1  # Índice do menor elemento

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Troca os elementos

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Coloca o pivô na posição correta
    return i + 1

# Implementação do quicksort
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# Gera um array de 100 mil números inteiros aleatórios
array = [random.randint(0, 1000000) for _ in range(100000)]

# Chama o algoritmo de quicksort
quicksort(array, 0, len(array) - 1)

# Verifica se o array está ordenado
print(array[:10])  # Mostra os primeiros 10 elementos para confirmação
