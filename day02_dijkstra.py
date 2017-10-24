import heapq

def dijkstra(graph, source):
    visited = set([source])
    distances = {source:0}
    cut_edges = [(el[1],(source, el[0])) for el in graph[source]] #for compatibility with heapq
    heapq.heapify(cut_edges)
    while len(visited) != len(graph):
        (weight, edge) = heapq.heappop(cut_edges)
        next_vertex = edge[1]
        distances[next_vertex] = weight
        visited.add(next_vertex)
        cut_edges = [el for el in cut_edges if el[1][1] != next_vertex]
        cut_edges += [(weight + el[1], (next_vertex, el[0])) for el in graph[next_vertex] if el[0] not in visited]
        heapq.heapify(cut_edges)
    return distances

def test_dijkstra():
    graph = {0: [(1, 1), (2, 8), (3, 2)],
            1: [(4, 6)],
            2: [(4, 1)],
            3: [(2, 3)],
            4:[]}
    res = {0: 0, 1: 1, 3: 2, 2: 5, 4: 6}
    assert dijkstra(graph, 0) == res
