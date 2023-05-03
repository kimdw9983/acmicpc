import sys, heapq
input = sys.stdin.readline
V, E = map(int, input().split())

graph = [list() for _ in range(V+1)]
for _ in range(E) :
  a, b, w = map(int, input().split())
  graph[a].append((w, b))
  graph[b].append((w, a))

heap = []
def add_edge(u) :
  global heap
  for l in graph[u] :
    heapq.heappush(heap, l)

INF = int(2e9)
check = [-1] + [INF] * V
def prim() :
  weight = 0
  heapq.heappush(heap, (0, 1))
  for i in range(1, V+1) :
    w = int(2e9)
    while heap :
      top = heap[0]
      v = top[1]

      if check[v] == INF :
        w = top[0]
        break
      heapq.heappop(heap)

    weight += w
    check[v] = w
    add_edge(v)
  return weight

print(prim() - max(check))