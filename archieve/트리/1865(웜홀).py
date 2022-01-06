import sys
input = sys.stdin.readline
TC = int(input())
INF = int(1e9)

for _ in range(TC) :
	N, M, W = map(int, input().split())
	edges = []

	for i in range(M+W) :
		S, E, T = map(int, input().split())
		edges.append((S, E, T if i < M else -T))
		if i < M :
			edges.append((E, S, T))

	DP = [INF, 0] + [INF] * (N-1) #시작 정점 = 1
	HAS_CYCLE = False
	for n in range(N) :
		for u, v, w in edges :
			if DP[v] > DP[u] + w :
				DP[v] = DP[u] + w
				if n == N-1 : #벨만법을 사용할땐 음의 사이클을 확인해야 한다.
					HAS_CYCLE = True

	sys.stdout.write("YES\n" if HAS_CYCLE else "NO\n")