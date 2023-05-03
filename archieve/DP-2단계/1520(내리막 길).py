import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
M, N = map(int, input().split())

l = [[*map(int, input().split())] for _ in range(M)]
DP = [[-1] * N for _ in range(M)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y) :
  if DP[x][y] != -1 : #탐색하지 않은 곳만 탐색
    return DP[x][y]
  if x == M-1 and y == N-1 : #맵크기가 1x1인경우
    return 1

  DP[x][y] = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if not (0 <= nx < M and 0 <= ny < N) : continue
    if l[nx][ny] >= l[x][y] : continue
      
    DP[x][y] += DFS(nx, ny)

  return DP[x][y]
  
print(DFS(0, 0))