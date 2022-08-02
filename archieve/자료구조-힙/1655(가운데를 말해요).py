import sys, heapq
input = sys.stdin.readline

N = int(input())
rq = [] #평균값보다 더 큰 값이 들어가는 최소 힙
lq = []

mid = int(input())
answer = [mid]
for T in range(N-1) :
	x = int(input())
	if mid < x :
		heapq.heappush(rq, x)
		if len(rq)-1 != len(lq) :
			heapq.heappush(lq, -mid)
			mid = heapq.heappop(rq)
	else :
		heapq.heappush(lq, -x)
		if len(rq) == len(lq) - 1 :
			heapq.heappush(rq, mid)
			mid = -heapq.heappop(lq)
	answer.append(mid)
sys.stdout.write("\n".join(map(str, answer)))