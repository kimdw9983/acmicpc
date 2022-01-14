import collections
A, B = map(int, input().split())

check = {A : 1} #간선 : 깊이+1
queue = collections.deque([A])
while True :
		if not queue :
				print(-1)
				break

		v = queue.popleft()
		if v == B :
				print(check[v])
				break

		for c in (v*2, v*10+1) :
				if c <= int(1e9) and not c in check :
						check[c] = check[v] + 1
						queue += [c]