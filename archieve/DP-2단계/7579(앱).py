import sys
input = sys.stdin.readline
N, K = map(int, input().split())
W = [*map(int, input().split())]
V = [*map(int, input().split())]
Vsum = sum(V)
dp = [[0] * (Vsum+1) for _ in range(N)]

for i in range(N):
  for j in range(1, Vsum+1):
    w = W[i]
    v = V[i]
    if j < v:
      X = dp[i-1][j]
      dp[i][j] = X
    else:
      X = max(w + dp[i-1][j-v], dp[i-1][j])
      dp[i][j] = X
    if X >= K :
      answer = j
      break
      
print(answer)