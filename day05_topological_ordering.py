def get_topological_ordering(graph, source):
    visited = set()
    current_label = [len(graph)]
    topological_ordering = {}
    def run_dfs(graph, source):
        visited.add(source)
        for v in graph[source]:
            if v not in visited:
                run_dfs(graph, v)
        topological_ordering[source] = current_label[0]
        current_label[0] = current_label[0] - 1

    run_dfs(graph, source)
    return topological_ordering

def test_get_topological_ordering():
    graph = {0: [1, 2],
            1: [4],
            2: [3],
            3: [2],
            4:[]}
    assert (get_topological_ordering(graph, 0)) == {4: 5, 1: 4, 3: 3, 2: 2, 0: 1}
