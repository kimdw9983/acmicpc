import sys, heapq
input = sys.stdin.readline
N, K = map(int, input().split())
V = []
C = []

for _ in range(N) : #likely to pop
	heapq.heappush(V, tuple(map(int, input().split())))

for _ in range(K) : #unlikely to pop
	C.append(int(input()))
C.sort()

tmp = []
answer = 0
for c in C :
	while V and c >= V[0][0] :#담을수 있는걸 가치가 높은것부터 전부 고려
		heapq.heappush(tmp, -heapq.heappop(V)[1])
	
	if tmp : #가방에는 한개씩 담음
		answer -= heapq.heappop(tmp)
	elif not V :
		break

print(answer)