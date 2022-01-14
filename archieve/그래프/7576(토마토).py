from collections import deque
import sys
input = sys.stdin.readline
M, N = map(int, input().split())

graph = []
check = [] #익힐 토마토의 리스트
for T in range(N) :
		l = [*map(int, input().split())]
		for i, v in enumerate(l) :
				if v == 1 :
						check.append((T, i))
		graph.append(l)

def ripe(pos):
		r, c = pos

		if c+1 < M and not graph[r][c+1] :
				graph[r][c+1] = 1
				yield (r, c+1)
		if r+1 < N and not graph[r+1][c] :
				graph[r+1][c] = 1
				yield (r+1, c)
		if c > 0 and not graph[r][c-1] :
				graph[r][c-1] = 1
				yield (r, c-1)
		if r > 0 and not graph[r-1][c] :
				graph[r-1][c] = 1
				yield (r-1, c)
		
level = 0
Q = deque(check)
while Q :
		nextQ = deque()
		while Q :
				v = Q.popleft()
				tmp = ripe(v)
				nextQ += tmp

		#print(*graph, "\n", sep="\n")
		level += 1
		Q += nextQ

valid = True
for l in graph :
		for v in l :
				if not v :
						valid = False
						break

if valid :
		print(level-1)
else : 
		print(-1)