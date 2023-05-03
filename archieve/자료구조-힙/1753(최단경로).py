import sys, heapq
input = sys.stdin.readline
V, E = map(int, input().split())

INF = 1234567891
graph = [[] for _ in range(V+1)]
S = int(input())

for _ in range(E) :
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

heap = []
W = [INF] * S + [0] + [INF] * (V-S)

heapq.heappush(heap, (0, S))
while heap:
    w, v = heapq.heappop(heap)
    if W[v] < w : #기록된것보다 가중치가 더 큰 경우
        continue

    for wa, n in graph[v] :
        if w + wa < W[n] : #가중치를 더한것이 기록된것보다 작은경우
            W[n] = w + wa
            heapq.heappush(heap, (w+wa, n))

for v in W[1:] :
    sys.stdout.write(("INF" if v == INF else str(v)) + "\n")