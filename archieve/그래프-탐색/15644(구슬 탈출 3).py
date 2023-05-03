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

dX = [-1, 0, 1, 0] #URDL
dY = [0, 1, 0, -1]
def move(x, y, i) :
  count = 0
  dx = dX[i]; dy = dY[i]
  while grid[x + dx][y + dy] != '#' and grid[x][y] != 'O':
      x += dx
      y += dy
      count += 1
  return x, y, count

Q = collections.deque()
Q.append((R, B, ""))
while Q :
  R, B, his = Q.popleft()
  if len(his) == 10 : continue

  for i in range(4) :
    xR = move(R[0], R[1], i)
    xB = move(B[0], B[1], i)
    if xR[0] == xB[0] and xR[1] == xB[1] and not grid[xB[0]][xB[1]] == "O": 
      if xR[2] > xB[2] :
        xR = (xR[0]-dX[i], xR[1]-dY[i], xR[2] - 1)
      else :
        xB = (xB[0]-dX[i], xB[1]-dY[i], xB[2] - 1)

    if xR[2] == xB[2] == 0 : continue

    nR = grid[xR[0]][xR[1]]
    nB = grid[xB[0]][xB[1]]

    if nB == "O" : continue #파란구슬이 들어가는 경우 제외.
    if nR == "O" : 
      his += str(i)
      print(len(his))
      for c in his :
        sys.stdout.write("URDL"[int(c)])
      sys.exit(0) 

    Q.append(((xR[0], xR[1]), (xB[0], xB[1]), his+str(i)))

print(-1)