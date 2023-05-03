N, K = map(int, input().split())
W = [0] * (N+1)
V = [0] * (N+1)
DP = [[0] * (K+1) for _ in range(N+1)]

for i in range(N) :
  W[i+1], V[i+1] = map(int, input().split())

for i in range(1, N+1):
  for j in range(1, K+1):
    w = W[i]
    v = V[i]

    if j < w:
      DP[i][j] = DP[i-1][j]
    else:
      DP[i][j] = max(v + DP[i-1][j-w], DP[i-1][j])

print(DP[N][K])

#############################시간초과 난 풀이
N, K = map(int, input().split())
W = [0] * N
V = [0] * N

for i in range(N) :
  W[i], V[i] = map(int, input().split())

memo = dict()
def DP(*key) :
  n, w = key
  if(n == 0 or w == 0) :
    return 0
  
  left = (n-1, w)
  if left not in memo :
    memo[left] = DP(*left)
  lvalue = memo[left]

  right = (n-1, w-W[n])
  if right not in memo :
    memo[right] = DP(*right)
  rvalue = memo[right]

  return lvalue if (W[n] > w) else max(lvalue, V[n] + rvalue)

print(DP(N-1, K))