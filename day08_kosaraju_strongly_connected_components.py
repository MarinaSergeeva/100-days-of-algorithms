def get_strongly_connected_components(graph):
    reversed_graph = get_reversed_graph(graph)
    visited = set()
    strongly_connected_components = []
    for v in get_ordering_dfs(graph):
        if v not in visited:
            new_scc = run_dfs(graph, v, [], visited)
            strongly_connected_components.append(new_scc)
    return strongly_connected_components

def get_reversed_graph(graph):
    reversed_graph = {}
    for start, vertex_list in graph.items():
        for end in vertex_list:
            reversed_graph[end] = reversed_graph.get(end, []) + [start]
    return reversed_graph

def get_ordering_dfs(graph):
    visited = set()
    ordering = []
    for v in graph:
        if v not in visited:
            run_dfs(graph, v, ordering, visited)
    return ordering

def run_dfs(graph, source, ordering, visited):
    visited.add(source)
    children = set([source])
    for v in graph[source]:
        if v not in visited:
            children |= run_dfs(graph, v, ordering, visited)
    ordering.append(source)
    return children

def test_get_strongly_connected_components():
    graph = {1: [5],
            2: [3],
            3: [4],
            4: [2, 5],
            5: [6],
            6: [1, 9],
            7: [8],
            8: [9],
            9: [7]}
    assert get_strongly_connected_components(graph) == [{8, 9, 7}, {1, 5, 6}, {2, 3, 4}]

def test_get_reversed_graph():
    graph = {1: [5],
            2: [3],
            3: [4],
            4: [2, 5],
            5: [6],
            6: [1, 9],
            7: [8],
            8: [9],
            9: [7]}
    assert get_reversed_graph(graph) == {5: [1, 4], 3: [2], 4: [3], 2: [4], 6: [5], 1: [6], 9: [6, 8], 8: [7], 7: [9]}

def test_get_ordering_dfs():
    graph = {1: [5],
            2: [3],
            3: [4],
            4: [2, 5],
            5: [6],
            6: [1, 9],
            7: [8],
            8: [9],
            9: [7]}
    assert get_ordering_dfs(graph) == [8, 7, 9, 6, 5, 1, 4, 3, 2]

if __name__ == "__main__":
    graph = {1: [5],
            2: [3],
            3: [4],
            4: [2, 5],
            5: [6],
            6: [1, 9],
            7: [8],
            8: [9],
            9: [7]}
    print(get_strongly_connected_components(graph))
