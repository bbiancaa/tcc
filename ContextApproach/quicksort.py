def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Escolhe o elemento do meio como pivô
        left = [x for x in arr if x < pivot]  # Elementos menores que o pivô
        middle = [x for x in arr if x == pivot]  # Elementos iguais ao pivô
        right = [x for x in arr if x > pivot]  # Elementos maiores que o pivô
        return quicksort(left) + middle + quicksort(right)

# Exemplo de uso
if __name__ == "__main__":
    import random
    arr = [random.randint(0, 1000000) for _ in range(100000)]  # Array com 100 mil números aleatórios
    print("Array ordenado:", arr[:100], "...") 
    sorted_arr = quicksort(arr)
    # print("Array ordenado:", sorted_arr[:1000], "...")  # Exibindo apenas os 10 primeiros elementos
