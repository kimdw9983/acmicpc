def solve() :
	k = int(input())
	
	acc = [0]
	sum = 0
	for v in input().split():
		sum += int(v)
		acc.append(sum)
		
	dp = [[0] * 501 for _ in range(501)]
	for d in range(1, k) :
		for a in range(1, 1+k-d) :
			b = a + d
			dp[a][b] = 99999999
			for m in range(a, b) :
				dp[a][b] = min(dp[a][b], dp[a][m] + dp[m+1][b] + acc[b] - acc[a-1])

	print(dp[1][k])
	
import sys
input = sys.stdin.readline
T = int(input())

for TC in range(T) :
	solve()