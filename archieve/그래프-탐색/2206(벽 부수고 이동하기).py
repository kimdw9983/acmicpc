import collections, sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[*map(int, input().rstrip())] for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

Q = collections.deque()
Q.append((0, 0, 0))
visited[0][0][0] = 1
answer = -1
while Q :
  x, y, c = Q.popleft()
  if x == N - 1 and y == M - 1: #도착했을 경우
    answer = visited[x][y][c]
    break

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
      continue

    if graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
      Q.append((nx, ny, c))
      visited[nx][ny][c] = visited[x][y][c] + 1

    if graph[nx][ny] == 1 and c == 0: 
      #벽을 만났을 경우 부수면서 이동
      Q.append((nx, ny, c+1))
      visited[nx][ny][c+1] = visited[x][y][c] + 1

print(answer)