import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
IN = [-1] + [0] * N #진입차수 갯수
for _ in range(M) :
	A, B = map(int, input().split())
	graph[A].append(B)
	IN[B] += 1

Q = []
dp = [0] * (N+1)
for i, e in enumerate(IN) :
	if not e :
		Q.append(i)
heapq.heapify(Q)

answer = []
while Q :
	v = heapq.heappop(Q)
	answer.append(v)

	for e in graph[v] :
		IN[e] -= 1
		if not IN[e] :
			heapq.heappush(Q, e)

sys.stdout.write(" ".join(map(str, answer)))