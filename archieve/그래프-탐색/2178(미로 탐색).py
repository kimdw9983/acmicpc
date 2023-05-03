import sys, collections
input = sys.stdin.readline
N, M = map(int, input().split())
grid = [[0] * M for _ in range(N)]

for i in range(N) :
    for j, c in enumerate(*input().rsplit()) :
        if c == '1' :
            grid[i][j] = 0
        else :
            grid[i][j] = 1

def seek(pos, cnt):
    r, c = pos
    
    if r+1 < N and not grid[r+1][c] : #위
        grid[r+1][c] = cnt
        yield (r+1, c)
    if c > 0 and not grid[r][c-1] : #왼
        grid[r][c-1] = cnt
        yield (r, c-1)
    if c+1 < M and not grid[r][c+1] : #오른쪽
        grid[r][c+1] = cnt
        yield (r, c+1)
    if r > 0 and not grid[r-1][c] : #아래
        grid[r-1][c] = cnt
        yield (r-1, c)

Q = collections.deque()
Q.append((0, 0))
grid[0][0] = 1
level = 2

while Q :
    nextQ = collections.deque()
    while Q :
        pos = Q.popleft()
        nextQ += seek(pos, level)

    level += 1
    Q += nextQ

print(grid[N-1][M-1])
######################################################
from collections import deque
import sys

N, M = map(int, input().split())
input = sys.stdin.readline
graph = []

for _ in range(N):
  graph.append([*map(int, input().rstrip())])

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

queue = deque()
queue.append((0, 0))
while queue:
  x, y = queue.popleft()

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or nx >= N or ny < 0 or ny >= M:
      continue

    if graph[nx][ny] == 0:
      continue

    if graph[nx][ny] == 1:
      graph[nx][ny] = graph[x][y] + 1
      queue.append((nx, ny))

print(graph[N-1][M-1])