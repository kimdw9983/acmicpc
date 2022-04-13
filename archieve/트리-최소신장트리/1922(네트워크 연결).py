import sys, heapq
input = sys.stdin.readline
V = int(input().rstrip()) 
E = int(input().rstrip())

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

check = [False] * (V+1)
def prim() :
	weight = 0
	heapq.heappush(heap, (0, 1))
	for i in range(1, V+1) :
		w = int(2e9)
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