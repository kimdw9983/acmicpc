NUM_NODES = 10
g = [[] for i in range(NUM_NODES + 1)]


def connect(g, n1, n2):
    g[n1].append(n2)
    g[n2].append(n1)  #유향(directed)그래프 일경우 해당 없음.


def DFS(g, start):
  stack = [start]
  check = [False for _ in range(NUM_NODES + 1)]

  while stack:
    v = stack.pop()
    if not check[v]:
      check[v] = True  #들어갔음을 확인
      stack += g[v]  #해당 노드에 연결된 간선 추가

def DFS_tree(start):
  q = [start]
  while q:
    v = q.pop()
    for i in g[v]:
      if parent[i] == 0:
        parent[i] = v
        q.append(i)


def BFS(g, start):
    Q = [start]#collections.deque([start])
    check = [False for _ in range(NUM_NODES + 1)]
    check[start] = True

    while Q:
        v = Q.pop()
        for i in reversed(g[v]): 
            if not check[i]:
                check[i] = True
                Q = [i] + Q


M, N = 2, 3
g = [[0] * M for i in range(N)]

#미로찾기 N이 세로여야하고, M이 가로여야 함.
#r이 세로, c가 가로
def ripe(pos):
    r, c = pos

    if c+1 < M and not g[r][c+1] :
        g[r][c+1] = 1
        yield (r, c+1)
    if r+1 < N and not g[r+1][c] :
        g[r+1][c] = 1
        yield (r+1, c)
    if c > 0 and not g[r][c-1] :
        g[r][c-1] = 1
        yield (r, c-1)
    if r > 0 and not g[r-1][c] :
        g[r-1][c] = 1
        yield (r-1, c)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Q = list()
Q.append((0, 0))
while Q:
  x, y = Q.pop()

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if not (0 <= nx < N and 0 <= ny < M) : continue #경계
    if g[nx][ny] == 0:continue  #못갈때

    if g[nx][ny] == 1: #갈수 있을때
      Q.append((nx, ny)) 