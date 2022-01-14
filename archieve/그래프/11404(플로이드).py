import sys
input = sys.stdin.readline
V = int(input())
E = int(input())

INF = 1234567891
graph = [[INF] * i + [0] + [INF] * (V-i-1) for i in range(V)]

for _ in range(E) :
		r, c, w = map(int, input().split())
		graph[r-1][c-1] = min(graph[r-1][c-1], w)

for m in range(V) : #중간
		for a, l in enumerate(graph) : #... in range(V) 로 구현-> 200ms
				for b, v in enumerate(l) : #enumerate로 구현 -> 184ms
						l[b] = min(v, l[m] + graph[m][b])

for i, l in enumerate(graph) :
		for j, v in enumerate(l) :
				sys.stdout.write("0 " if v == INF else str(v) + " ")
		sys.stdout.write("\n")