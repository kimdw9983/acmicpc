import sys, heapq
input = sys.stdin.readline
V = int(input())

INF = 0
graph = [[] for _ in range(V+1)]

for _ in range(V-1) :
		u, v, w = map(int, input().split())
		graph[u].append((-w, v))
		graph[v].append((-w, u))

def farthest_from(start) :
		heap = []
		W = [0] * (V+1)
		m = (0, start) #가장 긴 경로의 끝의 인덱스
		visited = [False] * (V+1)
		visited[start] = True
		heapq.heappush(heap, (0, start))
		while heap:
				w, v = heapq.heappop(heap)

				for wa, n in graph[v] :
						if w+wa < W[n] and not visited[n]:
								visited[n] = True
								W[n] = w+wa
								m = min(m, (w+wa, n), key=lambda x: x[0])
								heapq.heappush(heap, (w+wa, n))
		
		return m

print(-farthest_from(farthest_from(1)[1])[0])