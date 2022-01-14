import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
PRICE = []
for _ in range(N) :
	PRICE.append(tuple(map(int, input().split())))

NONE = -1
memo = [[NONE] * 3 for _ in range(N-1)]
memo[0][0] = (PRICE[0][0], 0)
memo[0][1] = (PRICE[0][1], 1)
memo[0][2] = (PRICE[0][2], 2)

def C(n, c) :
	if memo[n][c] != NONE :
		return memo[n][c]
	else :
		A = C(n-1, (c+1) % 3)[0]
		B = C(n-1, (c+2) % 3)[0]
		if A < B :
			memo[n][c] = (A + PRICE[n][c], (c+1) % 3)
		else :
			memo[n][c] = (B + PRICE[n][c], (c+2) % 3)

		return memo[n][c]

for i in range(3) :
	C(N-2, i)

answer = int(1e9)
for i in range(3) :
	X = memo[-1][i]
	for j in range(3) :
		if i == j or j == X[1] : continue #X[-1]
		answer = min(answer, X[0] + PRICE[-1][j]) 
print(answer)