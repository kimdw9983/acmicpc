import heapq
N, K = map(int, input().split())
MAX = 100000
W = [-1] * (MAX+1)
heap = [(0, N)]
Po2 = [2**i for i in range(1, 17)]

while heap : 
		w, v = heapq.heappop(heap)
		if v == K :
				print(w)
				break
		
		for m in Po2 :
				nv = v*m
				if nv > MAX :
						break
				if W[nv] == -1 :
						W[nv] = w
						heapq.heappush(heap, (w, nv))

		for nv in (v+1, v-1) :
				if 0 <= nv <= MAX and W[nv] == -1 :
						W[nv] = w + 1
						heapq.heappush(heap, (w + 1, nv))
###############################################
def BOJ13549():
		def c(n,k):
				if n>= k:
						return n-k
				elif k == 1:
						return 1
				elif k % 2:
						return 1 + min(c(n,k-1),c(n, k+1))
				else: # k%2 == 0
						return min(k-n, c(n,k//2))
		n, k = map(int,input().split())
		print(c(n,k))
BOJ13549()