import heapq
from day23_union_find import UnionFind
from day24_kruskal import get_edges

def get_clusters(graph, number_of_clusters):
    """Kruscal algorithm to find a minimum spanning tree"""
    # assume that there is only one connected component
    nodes = list(graph.keys())
    edges_heap = get_edges(graph)
    heapq.heapify(edges_heap)
    groups = UnionFind(nodes)
    while groups.count_groups() > number_of_clusters:
        _, edge = heapq.heappop(edges_heap)
        while groups.find(edge[0]) == groups.find(edge[1]):
            # adding the smallest edge that does not create cycle
            _, edge = heapq.heappop(edges_heap)
        groups.union(edge[0], edge[1])
    return groups.get_groups()

def test_get_clusters():
    graph0 = {0: [(1, 1), (2, 8), (3, 2)],
              1: [(0, 1), (4, 6)],
              2: [(0, 8), (3, 3), (4, 1)],
              3: [(0, 2), (2, 3)],
              4:[(1, 6), (2, 1)]}
    assert get_clusters(graph0, 3) == [[0, 1], [2, 4], [3]]
    assert get_clusters(graph0, 2) == [[0, 1, 3], [2, 4]]
    graph1 = {0:[(1, 5), (3, 1)],
              1: [(0, 5), (3, 2), (2, 6)],
              2: [(1, 6), (3, 10), (4, 7)],
              3: [(0, 1), (1, 2), (2, 10), (4, 2)],
              4: [(2, 7), (3, 2)]}
    assert get_clusters(graph1, 2) == [[0, 3, 1, 4], [2]]

if __name__ == "__main__":
    test_get_clusters()
