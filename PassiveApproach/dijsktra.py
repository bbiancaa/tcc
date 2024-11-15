import heapq

def dijkstra(graph, start):
    # Dicionário que irá armazenar a menor distância de start para cada nó
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Fila de prioridade para escolher o próximo nó com menor distância conhecida
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Se a distância retirada da fila for maior que a registrada, ignore
        if current_distance > distances[current_node]:
            continue
        
        # Verifica cada vizinho do nó atual
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # Se a nova distância for menor que a distância registrada, atualize
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Exemplo de criação de um grafo com 10 mil nós e arestas aleatórias
import random

# Criação de um grafo aleatório
graph = {i: [] for i in range(10000)}
for i in range(10000):
    # Adiciona arestas para alguns vizinhos aleatórios
    for _ in range(random.randint(1, 5)):
        neighbor = random.randint(0, 9999)
        weight = random.randint(1, 20)
        if neighbor != i:
            graph[i].append((neighbor, weight))

# Execução do algoritmo de Dijkstra a partir do nó 0
distances = dijkstra(graph, 0)
print("Menores distâncias a partir do nó 0 calculadas com sucesso!")
