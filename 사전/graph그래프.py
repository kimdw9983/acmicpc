NUM_NODES = 10
graph = [[] for i in range(NUM_NODES + 1)]


def connect(graph, n1, n2):
    graph[n1].append(n2)
    graph[n2].append(n1)  #유향(directed)그래프 일경우 해당 없음.


def DFS(graph, start):
    stack = [start]
    check = [False for _ in range(NUM_NODES + 1)]

    while stack:
        v = stack.pop()
        if not check[v]:
            check[v] = True  #들어갔음을 확인
            stack += graph[v]  #해당 노드에 연결된 간선 추가

def DFS_graph(start):
    q = [start]
    while q:
        v = q.pop()
        for i in graph[v]:
            if parent[i] == 0:
                parent[i] = v
                q.append(i)


def BFS(graph, start):
    queue = [start]#collections.deque([start])
    check = [False for _ in range(NUM_NODES + 1)]
    check[start] = True

    while queue:
        v = queue.pop()
        for i in reversed(graph[v]): 
            if not check[i]:
                check[i] = True
                queue = [i] + queue


M, N = 2, 3
graph = [[0] * M for i in range(N)]

#미로찾기 N이 세로여야하고, M이 가로여야 함.
#r이 세로, c가 가로
def ripe(pos):
    r, c = pos

    if c+1 < M and not graph[r][c+1] :
        graph[r][c+1] = 1
        yield (r, c+1)
    if r+1 < N and not graph[r+1][c] :
        graph[r+1][c] = 1
        yield (r+1, c)
    if c > 0 and not graph[r][c-1] :
        graph[r][c-1] = 1
        yield (r, c-1)
    if r > 0 and not graph[r-1][c] :
        graph[r-1][c] = 1
        yield (r-1, c)