import os, io, sys, bisect
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
N = int(input())
DATA = [*map(int, input().split())]
dp = [0] * N
l = [-int(2e9)]
MAX = 0 

for i, n in enumerate(DATA) : 
	if l[-1] < n: 
		l.append(n)
		dp[i] = len(l) - 1
		MAX = dp[i]
	else:
		dp[i] = bisect.bisect_left(l, n) 
		l[dp[i]] = n 
print(MAX)

res = []
for i, v in enumerate(dp[::-1]):
	if v == MAX:
		res.append(DATA[N-i-1])
		MAX -= 1
sys.stdout.write(" ".join(map(str, res[::-1])))