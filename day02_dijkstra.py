import heapq
from math import inf

def dijkstra(graph, source):
    visited = set([source])
    distances = {v: inf for v in graph}
    # parents = {v: None for v in graph}
    distances[source] = 0
    for (v, w) in graph[source]:
        distances[v] = w
        # parents[v] = source
    vertices_heap = [(w, v) for (v, w) in graph[source]]
    heapq.heapify(vertices_heap)
    while len(visited) != len(graph):
        (weight, next_vertex) = heapq.heappop(vertices_heap)
        while next_vertex in visited:
            (weight, next_vertex) = heapq.heappop(vertices_heap)
        distances[next_vertex] = weight
        visited.add(next_vertex)
        for (v, w) in graph[next_vertex]:
            if v not in visited:
                new_distance = w + distances[next_vertex]
                if new_distance < distances[v]:
                    distances[v] = new_distance
                    # parents[v] = next_vertex
                    heapq.heappush(vertices_heap, (new_distance, v))
    return distances

def test_dijkstra():
    graph = {0: [(1, 1), (2, 8), (3, 2)],
            1: [(4, 6)],
            2: [(4, 1)],
            3: [(2, 3)],
            4:[]}
    res = {0: 0, 1: 1, 3: 2, 2: 5, 4: 6}
    assert dijkstra(graph, 0) == res

if __name__ == "__main__":
    test_dijkstra()
