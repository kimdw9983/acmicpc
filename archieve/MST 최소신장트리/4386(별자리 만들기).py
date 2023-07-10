import sys, heapq, math
input = sys.stdin.readline
V = int(input().rstrip()) 

space = []
for _ in range(V) :
  space.append(tuple(map(float, input().split())))

heap = []
def add_edge(u) :
  global heap
  x1, y1 = space[u]
  for i, coord in enumerate(space) :
    if i == u : continue
    x2, y2 = space[i]
    d = math.hypot(x2-x1, y2-y1) #유클리드계에서 두점사이의 거리
    heapq.heappush(heap, (d, i))

check = [False] * V
def prim() :
  weight = 0
  heapq.heappush(heap, (0.0, 0))
  for i in range(V) :
    while heap :
      top = heap[0]
      v = top[1]

      if not check[v] :
        w = top[0]
        break
      heapq.heappop(heap)

    weight += w
    check[v] = True
    add_edge(v)
  return weight

print(prim())