def dfs(graph, source):
    visited = set()
    def run_dfs(graph, source):
        visited.add(source)
        # print(source)
        for v in graph[source]:
            if v not in visited:
                run_dfs(graph, v)

    run_dfs(graph, source)

def test_dfs():
    graph = {0: [1, 2],
            1: [4],
            2: [3],
            3: [2],
            4:[]}
    dfs(graph, 0)

if __name__ == "__main__":
    test_dfs()
