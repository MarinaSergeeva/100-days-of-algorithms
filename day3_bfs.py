import collections

def bfs(graph, source):
    visited = set()
    discovered = set([source])
    queue = collections.deque()
    queue.append(source)
    while queue:
        v = queue.popleft()
        visited.add(v)
        # print(v)
        for el in graph[v]:
            if el not in discovered:
                queue.append(el)
                discovered.add(el)
    return visited

def test_bfs():
    graph = {0: [1, 2],
            1: [4],
            2: [3],
            3: [2],
            4:[]}
    visited = bfs(graph, 0)

if __name__ == "__main__":
    test_bfs()
