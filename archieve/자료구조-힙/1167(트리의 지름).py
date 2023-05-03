import sys, heapq
input = sys.stdin.readline
V = int(input())

graph = [[] for _ in range(V)]
for T in range(V) :
    l = [*map(int, input().split()[:-1])]
    j = l[0] #염병
    k = 0
    for i in range(1, len(l)) :
        if i&1 :
            k = l[i] - 1
        else :
            graph[j-1].append((-l[i], k))

def farthest_from(start) :
    heap = []
    W = [0] * V
    m = (0, start) #가장 긴 경로의 끝의 인덱스
    visited = [False] * V
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
    
print(-farthest_from(farthest_from(0)[1])[0])