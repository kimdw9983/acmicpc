import sys, collections
input = sys.stdin.readline
deque = collections.deque

dr = [0, -1, 0, 1, 0]
dc = [0, 0, 1, 0, -1]

def solve() :
  H, W = map(int, input().split())
  grid = [input().rstrip() for _ in range(H)]

  keys = 0 #비트필드화
  for c in input().rstrip() :
    if ord(c) >= ord('a') :
      keys = keys | (1 << ord(c) - ord('a'))

  def has_key(k) :
    return keys & (1 << k) != 0

  def passable(r, c) :#빈공간, 문서, 열쇠, 문(열쇠 있을때만)
    x = grid[r][c] #ord('*') == 42
    return x in ('.', '$') or ord(x) >= 97 or (ord(x) >= 65 and has_key(ord(x)-65))

  Q = deque()
  def seek_edge(Q) : 
    Q.clear() #deque()로 매번 재정의 하는 것보다 메모리를 아낄 수 있다??
    for r in range(H) :
      for c in range(W) :
        if (r == 0 or r == H-1 or c == 0 or c == W-1) and passable(r, c) : #테두리 확인  
          Q.append((r, c))
    #print(Q)

  seek_edge(Q) 
  answer = 0 #열쇠의 갯수
  visited = [[False] * W for _ in range(H)]
  while Q :
    r, c = Q.popleft()

    for i in range(5):
      nr = r + dr[i]
      nc = c + dc[i]

      if nr <= -1 or nr >= H or nc <= -1 or nc >= W : #빌딩 바깥은 제외
        continue
      
      if visited[nr][nc] : #이미 본곳은 제외
        continue

      X = grid[nr][nc] #살펴볼 곳
      #print(nr, nc, X)
      if X == '.' : 
        visited[nr][nc] = True
        Q.append((nr, nc))
      elif X == '$' :
        answer += 1
        visited[nr][nc] = True
        Q.append((nr, nc))
      elif X == '*' :
        visited[nr][nc] = True
        continue
      elif ord(X) >= 97 : #열쇠
        #print("hm")
        if not has_key(ord(X) - 97) :
          #print("hhm")
          keys = keys | (1 << (ord(X) - 97))
          visited = [[False] * W for _ in range(H)]
          seek_edge(Q)
          answer = 0
          break
        else : 
          visited[nr][nc] = True
          Q.append((nr, nc))
      else :
        if has_key(ord(X)-65) :
          visited[nr][nc] = True
          Q.append((nr, nc))
  print(answer)

for T in range(int(input())) :
  solve()