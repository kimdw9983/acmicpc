import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
T = int(input())

def DFS(s, result) :
	visited[s] = True
	tmp.append(s)
	x = l[s]
	
	if visited[x]:
		if x in tmp:
			result += tmp[tmp.index(x):]
		return
	else:
		DFS(x, result)


for _ in range(T) :
	N = int(input())
	visited = [True] + [False] * N
	l = [-1] + [*map(int, input().split())]
	result = []

	for i in range(1, N+1) :
		if not visited[i] :
			tmp = []
			DFS(i, result)
	
	print(N - len(result))