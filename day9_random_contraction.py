import random

class Graph:
    def __init__(self, graph):
        self._graph = graph
        self.number_of_edges = sum([len(node_list) for node_list in graph.values()])

    def get_random_edge(self):
        number = random.randint(0, self.number_of_edges - 1)
        return self.get_ith_edge(number)

    def get_ith_edge(self, i):
        for key in self._graph:
            if i >= len(self._graph[key]):
                i -= len(self._graph[key])
            else:
                return (key, self._graph[key][i])

    def contract(self, edge):
        # update the count for number of edges in the graph
        self.number_of_edges = self.number_of_edges + - len(self._graph[edge[1]]) - len(self._graph[edge[0]])
        # merge two vertices and remove self-loops
        self._graph[edge[0]] = [el for el in self._graph[edge[0]] if el != edge[1]] + [v for v in self._graph[edge[1]] if v != edge[0]]
        self.number_of_edges = self.number_of_edges + len(self._graph[edge[0]])
        # update all references to the 2nd vertex with the label of the 1st
        for key, edges in self._graph.items():
            self._graph[key] = [el if el != edge[1] else edge[0] for el in edges]
        self._graph.pop(edge[1], None)

    def get_node_count(self):
        return len(self._graph)


def random_contraction(graph):
    myGraph = Graph(graph)
    while myGraph.get_node_count() > 2:
        edge = myGraph.get_random_edge()
        myGraph.contract(edge)
    return myGraph.number_of_edges

def test_random_contraction():
    random.seed(42)
    graph = {0: [1, 2],
            1: [4],
            2: [3],
            3: [2],
            4:[]}
    assert random_contraction(graph) == 1

if __name__ == "__main__":
    test_random_contraction()
