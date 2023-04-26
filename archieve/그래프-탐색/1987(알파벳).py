import sys
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[0]*M for _ in range(N)]
for i, l in enumerate(graph) :
	for j, v in enumerate(input().rstrip()) :	
		l[j] = v

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
memo = [False] * 26
answer = 0
def travel(level, x, y) :
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if 0 <= nx < N and 0 <= ny < M :
			v = ord(graph[nx][ny])-65
			if memo[v] : continue
			memo[v] = True
			travel(level+1, nx, ny)
			memo[v] = False

	global answer
	answer = max(answer, level)

memo[ord(graph[0][0])-65] = True
travel(1, 0, 0)
print(answer)