from copy import deepcopy
from math import inf

def floyd_warshall(graph):
    """Algorithm to find all-pairs shortest path. Returns a martix with shortest path between vertices.
    Takes graph in the adjacency matrix format as an input"""
    distances = deepcopy(graph)
    n = len(graph)
    for i in range(n):
        for j in range(n):
            if i != j and distances[i][j] == 0:
                distances[i][j] = inf
    for k in range(n): # consider only paths that go through vertices with index < k
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    return distances

def test_floyd_warshall():
    graph = [[0, 5, 0, 1, 0],
            [5, 0, 6, 2, 0],
            [0, 6, 0, 10, 7],
            [1, 2, 10, 0, 2],
            [0, 0, 7, 2, 0]]
    assert floyd_warshall(graph) == [[0, 3, 9, 1, 3],
                                    [3, 0, 6, 2, 4],
                                    [9, 6, 0, 8, 7],
                                    [1, 2, 8, 0, 2],
                                    [3, 4, 7, 2, 0]]

if __name__ == "__main__":
    test_floyd_warshall()
