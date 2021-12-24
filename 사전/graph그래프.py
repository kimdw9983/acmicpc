import pprint
from collections import defaultdict


class Graph(object):
    """ Graph data structure, undirected by default. """
    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """ Remove all references to node """
        for n, cxns in self._graph.items():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """ 모든 경로를 다 찾음(최적거리 아님) """
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


#https://stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python

connections = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'),
               ('F', 'C')]
g = Graph(connections, directed=True)
pretty_print = pprint.PrettyPrinter()
pretty_print.pprint(g._graph)

####################### 속도 개선 ##########################
NUM_NODES = 10
graph = [[] for i in range(NUM_NODES + 1)]


def connect(graph, n1, n2):
    graph[n1].append(n2)
    graph[n2].append(n1)  #유향(directed)그래프 일경우 해당 없음.


def DFS(graph, start):
    visited = []
    stack = [start]
    check = [False for _ in range(NUM_NODES + 1)]

    while stack:
        v = stack.pop()
        if not check[v]:
            check[v] = True  #들어갔음을 확인
            visited.append(v)
            stack += graph[v]  #해당 노드에 연결된 간선 추가

    return visited


def BFS(graph, start):
    visited = []
    queue = [start]
    check = [False for _ in range(NUM_NODES + 1)]
    check[start] = True

    while queue:
        v = queue.pop()
        visited.append(v)
        for i in reversed(graph[v]):  #deque를 불러와서 쓰기보다 list를 거꾸로 순회하는게 효율적이다.
            if not check[i]:
                check[i] = True
                queue = [i] + queue

    return visited
