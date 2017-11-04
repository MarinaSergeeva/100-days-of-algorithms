import heapq

def get_prim_mst(graph):
    # for a connected component
    # assume nodes labeled 0 to n - 1
    max_value = 1000000000000 # some large number
    mst = []
    start_vertex = list(graph.keys())[0]
    spinned_vertices = set([start_vertex])
    weights = [max_value for el in graph]
    weights[start_vertex] = 0
    parents = [None for el in graph]
    for (vertex, weight) in graph[start_vertex]:
        weights[vertex] = weight
        parents[vertex] = start_vertex
    vertices_heap = [(weight, vertex) for (vertex, weight) in graph[start_vertex]]
    heapq.heapify(vertices_heap)
    while len(spinned_vertices) < len(graph):
        (weight, new_vertex) = heapq.heappop(vertices_heap)
        # can have multiple instances for one vertex in the heap => need to do the check
        while new_vertex in spinned_vertices:
            weight, new_vertex = heapq.heappop(vertices_heap)
        spinned_vertices.add(new_vertex)
        mst.append(((parents[new_vertex], new_vertex), weight))
        for (v, w) in graph[new_vertex]:
            if v not in spinned_vertices:
                if w < weights[v]:
                    weights[v] = w
                    parents[v] = new_vertex
                    heapq.heappush(vertices_heap, (w, v))
    return mst

def test_get_prim_mst():
    graph = {0: [(1, 1), (2, 8), (3, 2)],
            1: [(4, 6)],
            2: [(4, 1)],
            3: [(2, 3)],
            4:[]}
    assert get_prim_mst(graph) == [((0, 1), 1), ((0, 3), 2), ((3, 2), 3), ((2, 4), 1)]
    graph1 = {0:[(1, 5), (3, 1)],
                1: [(0, 5), (3, 2), (2, 6)],
                2: [(1, 6), (3, 10), (4, 7)],
                3: [(0, 1), (1, 2), (2, 10), (4, 2)],
                4: [(2, 7), (3, 2)]}
    assert get_prim_mst(graph1) == [((0, 3), 1), ((3, 1), 2), ((3, 4), 2), ((1, 2), 6)]

if __name__ == "__main__":
    test_get_prim_mst()
