import sys, collections
input = sys.stdin.readline
H, W = map(int, input().split())

grid = []
visited = [[False] * W for _ in range(H)]
for x in range(H) :
  l = [*input().rstrip()]
  for y, c in enumerate(l) :
    if c == 'R' :
      R = (x, y)
    elif c == 'B' :
      B = (x, y)
  grid.append(l)

dX = [-1, 0, 1, 0] #아오위왼
dY = [0, 1, 0, -1]
def move(x, y, i) :
  count = 0 #이동량
  dx = dX[i]; dy = dY[i]
  while grid[x + dx][y + dy] != '#' and grid[x][y] != 'O':
      x += dx
      y += dy
      count += 1
  return x, y, count

Q = collections.deque()
Q.append((R, B, 0))
while Q :
  R, B, cnt = Q.popleft()
  if cnt == 10 : continue #이렇게 하면 DFS도 될듯?

  for i in range(4) :
    xR = move(R[0], R[1], i)
    xB = move(B[0], B[1], i)
    if xR[0] == xB[0] and xR[1] == xB[1] and not grid[xB[0]][xB[1]] == "O": 
      #공이 곂친 경우
      if xR[2] > xB[2] : #R의 이동량이 더 많았을 경우
        xR = (xR[0]-dX[i], xR[1]-dY[i], xR[2] - 1) #R을 역방향으로 한칸이동
      else :
        xB = (xB[0]-dX[i], xB[1]-dY[i], xB[2] - 1)

    if xR[2] == xB[2] == 0 : continue #해당 방향으로 어떤 공도 이동하지 못한 경우

    nR = grid[xR[0]][xR[1]]
    nB = grid[xB[0]][xB[1]]

    if nB == "O" : continue #파란구슬이 들어가는 경우 제외.
    if nR == "O" : print("1");sys.exit(0);

    Q.append(((xR[0], xR[1]), (xB[0], xB[1]), cnt+1))

print("0")