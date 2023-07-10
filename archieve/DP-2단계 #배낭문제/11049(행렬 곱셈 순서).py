import sys
input = sys.stdin.readline
N = int(input())
dp = [[0] * N for _ in range(N)]
M = []
for i in range(N) :
  M.append(tuple(map(int, input().split())))

INF = int(3e9)
for i in range(1, N) :
  for j in range(N-i):
    x = j + i
    dp[j][x] = INF
    for k in range(j, x):
      dp[j][x] = min(dp[j][x], dp[j][k] + dp[k+1][x] + M[j][0] * M[k][1] * M[x][1])
  
print(dp[0][N-1])