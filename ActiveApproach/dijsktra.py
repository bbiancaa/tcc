import heapq

def dijkstra(graph, start):
    # Inicializa a distância para todos os nós como infinito e a distância inicial como 0
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Fila de prioridade para manter os nós a serem processados
    priority_queue = [(0, start)]
    
    # Dicionário para armazenar o caminho mais curto
    previous_nodes = {node: None for node in graph}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Se a distância atual é maior do que a já encontrada, continua para o próximo
        if current_distance > distances[current_node]:
            continue
        
        # Verifica os vizinhos do nó atual
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Se a distância encontrada for menor, atualiza a menor distância e o caminho
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous_nodes

def shortest_path(graph, start, target):
    distances, previous_nodes = dijkstra(graph, start)
    
    # Reconstrói o caminho a partir do destino para a origem
    path = []
    current_node = target
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path = path[::-1]  # Inverte a lista para ter o caminho na ordem correta
    
    if path[0] == start:
        return path, distances[target]
    else:
        return None, float('infinity')

# Exemplo de uso
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3}
}

start = 'A'
target = 'E'
path, distance = shortest_path(graph, start, target)

print(f"Caminho mais curto de {start} para {target}: {path} com distância {distance}")
