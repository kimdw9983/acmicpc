import sys
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for i in range(N+1)]
check = [True] + [False for _ in range(N)]

for __ in range(M):
	n1, n2 = map(int, input().split())
	graph[n1].append(n2)
	graph[n2].append(n1)

def DFS(start):
	stack = [start]
	while stack:
		v = stack.pop()
		if not check[v]:
			check[v] = True
			stack += graph[v]

cnt = 0
while True :
	start = -1
	for i, v in enumerate(check) :
		if not v :
			start = i
			break
		
	if start == -1 :
		print(cnt)
		break
	else : 
		cnt += 1
		DFS(start)