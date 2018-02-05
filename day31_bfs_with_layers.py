"""
Find the length of the longest path in an unweighted graph from a specified vertex
"""

import collections

def bfs_with_layers(graph, source):
    visited = set()
    discovered = set([source])
    layer_count = 0
    next_layer = collections.deque()
    next_layer.append(source)
    while next_layer:
        layer_count += 1
        cur_layer = next_layer
        next_layer = collections.deque()
        #print("layer: ", layer_count, "vertices: ", cur_layer)
        while cur_layer:
            v = cur_layer.popleft()
            visited.add(v)
            for el in graph[v]:
                if el not in discovered:
                    next_layer.append(el)
                    discovered.add(el)
    return layer_count

def test_bfs_with_layers():
    graph = {0: [1, 2],
            1: [4],
            2: [3],
            3: [2],
            4:[]}
    layer_count = bfs_with_layers(graph, 0)
    assert layer_count == 3

if __name__ == "__main__":
    test_bfs_with_layers()
