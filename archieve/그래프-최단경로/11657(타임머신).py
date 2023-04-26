import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
edges = []
for i in range(M) :
	edges.append([*map(int, input().split())])

DP = [INF, 0] + [INF] * (N-1) #시작 정점 = 1
HAS_CYCLE = False
for n in range(N) :
	for u, v, w in edges :
		if DP[u] != INF and DP[v] > DP[u] + w :
			DP[v] = DP[u] + w
			if n == N-1 :
				HAS_CYCLE = True

if HAS_CYCLE :
	sys.stdout.write("-1\n")
else :
	for n in DP[2:] :
		sys.stdout.write("-1\n" if n >= INF else str(n)+"\n")