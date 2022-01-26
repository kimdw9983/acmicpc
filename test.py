import sys
input = sys.stdin.readline
N = int(input())
l = [[*map(int, input().split())] for _ in range(N)]

def TSP(graph):
	stack = [1]
	
	while stack:
		v = stack.pop()
		if not check[v]:
			check[v] = True	#들어갔음을 확인
			stack += graph[v]	#해당 노드에 연결된 간선 추가