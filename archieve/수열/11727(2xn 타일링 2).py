N = int(input())
DP = [1, 1] + [0] * (N-1)
for i in range(2, N+1) :
		DP[i] = DP[i-2]*2 + DP[i-1]

print(DP[N]%10007)
#A001045 Jacobsthal sequence 