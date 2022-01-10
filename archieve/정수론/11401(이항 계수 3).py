N, K = map(int, input().split())
P = 1000000007

dp = [1] * (N+1) #dp[i] = factorial(i) % P
for i in range(2, N+1) :
	dp[i] = dp[i-1] * i % P
A = dp[N]
b = (dp[K] * dp[N-K])%P 
B = pow(b, P-2, P)

print((A*B) % P)

"""
이렇게 하지 않으려는게 dp쓰는거.
A = 1#(1 mod P)
for n in range(1, N+1) :
	A *= n%P
	if n == K :
		k = A #K! mod P
	if n == N-K :
		N_k = A #(N-K)! mod P
"""

"""
import math
#왜 틀린지 몰?루
p = P-2
B = 1
dp = [b]
for i in range(p.bit_length()) :
	x = dp[-1]
	dp.append((x%p)**2%p)
	if p&(1<<i) : 
		B *= x
"""