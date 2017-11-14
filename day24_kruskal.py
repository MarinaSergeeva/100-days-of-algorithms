import heapq
from day23_union_find import UnionFind

def kruskal(graph):
    """Kruscal algorithm to find a minimum spanning tree"""
    # assume that there is only one connected component
    nodes = list(graph.keys())
    edges_heap = get_edges(graph)
    heapq.heapify(edges_heap)
    groups = UnionFind(nodes)
    mst = []
    while groups.count_groups() > 1:
        weight, edge = heapq.heappop(edges_heap)
        while groups.find(edge[0]) == groups.find(edge[1]):
            # adding the smallest edge that does not create cycle
            weight, edge = heapq.heappop(edges_heap)
        mst.append((edge, weight))
        groups.union(edge[0], edge[1])
    return mst

def get_edges(graph):
    """get weighted edges from adjacency list"""
    edges = []
    for v1 in graph:
        for v2, weight in graph[v1]:
            if v1 < v2:
                edges.append((weight, (v1, v2)))
    return edges

def test_krusal():
    graph0 = {0: [(1, 1), (2, 8), (3, 2)],
              1: [(0, 1), (4, 6)],
              2: [(0, 8), (3, 3), (4, 1)],
              3: [(0, 2), (2, 3)],
              4:[(1, 6), (2, 1)]}
    assert kruskal(graph0) == [((0, 1), 1), ((2, 4), 1), ((0, 3), 2), ((2, 3), 3)]
    graph1 = {0:[(1, 5), (3, 1)],
              1: [(0, 5), (3, 2), (2, 6)],
              2: [(1, 6), (3, 10), (4, 7)],
              3: [(0, 1), (1, 2), (2, 10), (4, 2)],
              4: [(2, 7), (3, 2)]}
    assert kruskal(graph1) == [((0, 3), 1), ((1, 3), 2), ((3, 4), 2), ((1, 2), 6)]

if __name__ == "__main__":
    test_krusal()
