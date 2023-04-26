import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
		M, N, K = map(int, input().split())

		graph = [[False] * M for i in range(N)]

		l = list()
		for _ in range(K) :
				X, Y = map(int, input().split())
				graph[Y][X] = True
				l.append((Y, X))
		
		cnt = 0
		while l : #DFS
				visited = set()
				stack = [l.pop(0)]
				cnt += 1
				
				while stack :
						Y, X = stack.pop()

						next = []
						if X+1 < M and graph[Y][X+1] and not (Y, X+1) in visited:
								next.append((Y, X+1))
						if Y+1 < N and graph[Y+1][X] and not (Y+1, X) in visited:
								next.append((Y+1, X))
						if X > 0 and graph[Y][X-1] and not (Y, X-1) in visited:
								next.append((Y, X-1))
						if Y > 0 and graph[Y-1][X] and not (Y-1, X) in visited:
								next.append((Y-1, X))

						visited.add((Y, X)) 
						#굳이 visited 안만들고 바로 l에서 뺄수도 있다? - X
						#list의 인덱스가 필요하고 set의 차집합을 사용해야 함
						if next :
								stack += next

				l = list(set(l) - visited)

		print(cnt)
######################################################################
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
		M, N, K = map(int, input().split())
		graph = [[False] * M for i in range(N)]

		for _ in range(K) :
				X, Y = map(int, input().split())
				graph[Y][X] = True
				
		cnt = 0
		for i in range(N) :
				for j in range(M) :
						if graph[i][j] : #i, j : 탐색용 index
								cnt += 1

								stack = [(i, j)]
								while stack :
										r, c = stack.pop() #r(세로), c(가로) : DFS용 index
										graph[r][c] = False

										next = []
										if c+1 < M and graph[r][c+1] :
												next.append((r, c+1))
										if r+1 < N and graph[r+1][c] :
												next.append((r+1, c))
										if c > 0 and graph[r][c-1] :
												next.append((r, c-1))
										if r > 0 and graph[r-1][c] :
												next.append((r-1, c))
										
										if next :
												stack += next
		
		print(cnt)