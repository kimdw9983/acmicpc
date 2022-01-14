import sys

input = sys.stdin.readline
N, M, S = map(int, input().split())

graph = [[] for i in range(N + 1)]

for __ in range(M):
		n1, n2 = map(int, input().split())
		graph[n1].append(n2)
		graph[n2].append(n1)

for edge in graph:
		edge.sort(reverse=True)


def DFS(start): #벡터형 그래프에서 사용
		visited = []
		stack = [start]
		check = [False for _ in range(N + 1)]
		while stack:
				v = stack.pop()
				if not check[v]:
						check[v] = True	#들어갔음을 확인
						visited.append(v)
						stack += graph[v]	#해당 노드에 연결된 간선 추가
		return visited


def BFS(start): #벡터형 그래프에서 사용
		visited = []
		queue = [start]
		check = [False for _ in range(N + 1)]
		check[start] = True
		while queue:
				v = queue.pop()
				visited.append(v)
				for i in graph[v][::-1]:	#deque를 불러와서 쓰기보다 list를 거꾸로 순회하는게 효율적이다.
						if not check[i]:
								check[i] = True
								queue = [i] + queue
		return visited


#visited 출력
sys.stdout.write(" ".join(map(str, DFS(S))) + "\n" + " ".join(map(str, BFS(S))))


