import heapq

def dijkstra(graph, start):
    # Número de nós no grafo
    n = len(graph)
    
    # Distâncias para os nós, inicializando com infinito
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Fila de prioridade (min-heap), iniciada com o nó de início e sua distância 0
    priority_queue = [(0, start)]  # (distância, nó)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Se a distância atual for maior que a distância registrada, ignoramos o nó
        if current_distance > distances[current_node]:
            continue
        
        # Explorar os vizinhos
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Só consideramos um novo caminho se ele for melhor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Exemplo de grafo ponderado representado como um dicionário de adjacência
# Cada nó aponta para outro nó e o peso da aresta
graph = {
    0: {1: 7, 2: 9, 3: 14},
    1: {0: 7, 2: 10, 4: 15},
    2: {0: 9, 1: 10, 3: 11, 4: 2},
    3: {0: 14, 2: 11, 4: 9},
    4: {1: 15, 2: 2, 3: 9},
}

# Encontrar o caminho mais curto a partir do nó 0
start_node = 0
shortest_paths = dijkstra(graph, start_node)

print(f"Caminhos mais curtos a partir do nó {start_node}:")
for node, dist in shortest_paths.items():
    print(f"Nó {node}: {dist}")
