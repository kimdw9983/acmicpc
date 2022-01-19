import sys, collections
input = sys.stdin.readline
T = int(input())

for _ in range(T) :
	N, K = map(int, input().split())
	graph = [[] for _ in range(N+1)]
	W = [-1] + [*map(int, input().split())]
	IN = [-1] + [0] * N #진입차수 갯수
	for _ in range(K) :
		X, Y = map(int, input().split())
		graph[X].append(Y)
		IN[Y] += 1

	Q = collections.deque()
	dp = [0] * (N+1)
	for i, e in enumerate(IN) :
		if not e :
			Q.append(i)
			dp[i] = W[i]

	s = int(input())
	while Q :
		v = Q.popleft()
		#if v == s : break
		for e in graph[v] :
			IN[e] -= 1
			dp[e] = max(dp[v] + W[e], dp[e])
			if not IN[e] :
				Q.append(e)
	print(dp[s])
#############################################################
#top-down memoization 풀이
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
	N, K = map(int, input().split())
	graph = [[] for _ in range(N+1)]
	W = [-1] + [*map(int, input().split())]

	for _ in range(K) :
		X, Y = map(int, input().split())
		graph[Y].append(X) #Y를 만드는데 필요한 건물들 저장

	memo = dict()
	#top-down 방식 dp에선 dict를 사용한다.
	#불필요한 키를 탐색할 필요가 없을경우 dict에 값을 추가할 필요가 없으므로
	#단, 최악의 케이스에선 딕셔너리의 키값을 해싱하는 함수와 
	#키 -> 해시값을 저장하는 메모리도 커지므로 
	#많은 문제에서 실질적인 이득을 보기는 힘들다고 본다.
	def C(k) :
		if k in memo :
			return memo[k]
		w = 0
		for e in graph[k] :
			acc = C(e) #k번째 건물을 짓는 시간의 누적합(최소 시간)
			w = max(w, acc)
		memo[k] = w + W[k]
		return memo[k]
			
	s = int(input())		
	C(s)
	print(memo[s])