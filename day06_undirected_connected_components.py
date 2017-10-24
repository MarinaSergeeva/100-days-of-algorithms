from day3_bfs import bfs

def get_undirected_connected_components(graph):
    """
    get undirected components for an undirected graph
    """
    visited = set()
    conneted_components = []
    for v in graph:
        if v not in visited:
            new_component = bfs(graph, v)
            visited |= new_component
            conneted_components.append(new_component)
    return conneted_components

def test_get_undirected_connected_components():
    graph = {0: [1, 2],
            1: [2],
            2: [1],
            3: [4],
            4:[]}
    assert get_undirected_connected_components(graph) == [{0, 1, 2}, {3, 4}]

if __name__ == "__main__":
    test_get_undirected_connected_components()
