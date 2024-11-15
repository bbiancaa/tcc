import heapq
import random

def dijkstra(graph, start):
    num_nodes = len(graph)
    distances = {node: float('infinity') for node in range(num_nodes)}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Se a distância atual já for maior do que a registrada, continue
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Se a nova distância for menor, atualiza a distância e adiciona na fila
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Criação de um grafo grande com 10 mil nós e arestas aleatórias
def create_large_graph(num_nodes=10000, num_edges=50000):
    graph = {i: [] for i in range(num_nodes)}
    for _ in range(num_edges):
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u != v:
            weight = random.randint(1, 10)
            graph[u].append((v, weight))
            graph[v].append((u, weight))  # Se for um grafo não-direcionado
    return graph

# Teste com 10 mil nós
graph = create_large_graph()
start_node = 0
distances = dijkstra(graph, start_node)
print("Cálculo de caminhos mais curtos completado.")
