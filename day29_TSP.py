"""Traveling saleseman problem implementation with dynamic programming"""

from itertools import combinations


def get_TSP(graph):
    """takes graph as distance matrix and returns optimal route and distance"""
    # row - from, column - to
    partial_cost = {}
    prev_vertices = {}
    n = len(graph)
    vertices = frozenset(range(1, n))
    for i in range(1, n):
        partial_cost[(i, frozenset())] = graph[0][i]
        prev_vertices[(i, frozenset())] = 0
    for i in range(1, n - 1):
        for s in frozenset(combinations(vertices, i)):
            s = frozenset(s)
            for j in vertices - s:
                partial_cost[j, frozenset(s)], prev_vertices[j, frozenset(s)] = get_min_cost_and_opt_prev(graph, partial_cost, j, s)
    partial_cost[0, vertices], prev_vertices[0, vertices] = get_min_cost_and_opt_prev(graph, partial_cost, 0, vertices)
    path = get_path(prev_vertices, vertices)
    return path, partial_cost[0, vertices]

def get_min_cost_and_opt_prev(graph, partial_cost, j, s):
    partial_cost_options = [(graph[k][j] + partial_cost[(k, frozenset(s - set([k])))], k) for k in s]
    (min_cost, best_prev) = min(partial_cost_options, key=lambda x: x[0])
    return min_cost, best_prev

def get_path(prev_vertices, vertices):
    """backtracking the optimal path"""
    cur_vertex = 0
    prev = prev_vertices[0, vertices]
    cur_vertices = vertices
    path = [0]
    while prev != 0:
        path.append(prev)
        cur_vertex = prev
        cur_vertices = frozenset(cur_vertices - set([cur_vertex]))
        prev = prev_vertices[cur_vertex, cur_vertices]
    return path[::-1]

def test_def_TSP():
    matrix1 = [[0, 1, 3, 2], [2, 0, 4, 7], [1, 5, 0, 1], [4, 3, 8, 0]]
    assert get_TSP(matrix1) == ([2, 3, 1, 0], 9)

if __name__ == "__main__":
    test_def_TSP()
