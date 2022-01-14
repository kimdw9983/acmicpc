import sys
input = sys.stdin.readline
N, M = map(int, input().split())

matrix = [[0] * N for i in range(N)]
s = [list(map(int, input().split())) for i in range(N)]

dp = [[0 for i in range(N + 1)] for i in range(N + 1)]
for i in range(N):
		for j in range(N):
				dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - dp[i][j]) + s[i][j]
print(*dp, sep="\n")

acc = 0 #accumulate
for i in range(N) :
		for j, v in enumerate(map(int, input().split())) :
				acc += v
				matrix[i+1][j+1] = acc

for T in range(M) :
		x1, y1, x2, y2 = map(int, input().split())
		
		sum = 0
		if y1 == x1 == 1:
				sum = matrix[x2][y2]
		elif y1 == 1 :
				for i in range(x2-x1) :
						sum += matrix[x2-i][y2] - matrix[x2-2-i][N]
				sum += matrix[0][y2]
		else :
				for i in range(x2-x1 + 1) :
						sum += matrix[x2-i][y2] - matrix[x2-i][y1-1]
				
		print(sum)
#####################################################
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

matrix = [[0] * N for i in range(N)]
s = [list(map(int, input().split())) for i in range(N)]

dp = [[0 for i in range(N+1)] for i in range(N+1)]
for i in range(N):
		for j in range(N):
				dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j] - dp[i][j]) + s[i][j]

for T in range(M) :
		x1, y1, x2, y2 = map(int, input().split())
		
		print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])