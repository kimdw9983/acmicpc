import sys
input = sys.stdin.readline

def swap(P1, P2) :
  P1, P2 = sorted([P1, P2], key= lambda x: (x[0], x[1]))
  return *P1, *P2

def compare(ax, ay, bx, by) :
  if ax == bx :  return ay <= by
  else : return ax <= bx 

def CCW(ax, ay, bx, by, cx, cy) :
  ccw = (bx-ax) * (cy-ay) - (cx-ax) * (by-ay)

  if ccw > 0 : return 1
  elif ccw < 0 : return -1
  return 0

def cross(x1, y1, x2, y2, x3, y3, x4, y4) :
  A = CCW(x1, y1, x2, y2, x3, y3) * CCW(x1, y1, x2, y2, x4, y4) 
  B = CCW(x3, y3, x4, y4, x1, y1) * CCW(x3, y3, x4, y4, x2, y2)
    
  if A == B == 0 : #4점 한직선
    x1, y1, x2, y2 = swap((x1, y1), (x2, y2))
    x3, y3, x4, y4 = swap((x3, y3), (x4, y4))
  
    return 1 if compare(x3, y3, x2, y2) and compare(x1, y1, x4, y4) else 0
  elif A == 0 or B == 0 : #3점 한직선
    return 1 if A <= 0 and B <= 0 else 0
  elif A < 0 and B < 0 : #교차하는 경우
    return 1
  else :
    return 0

def find(S, x):
  if S[x] < 0: return x
  S[x] = find(S, S[x])
  return S[x] 

def union(S, C, a, b):
  A = find(S, a)
  B = find(S, b)
  if A == B :  
    return

    S[B] = A
    C[A] += C[B]
    C[B] = 1

N = int(input())

roots = [-1] * N
counts = [1] * N
nodes = []
for _ in range(N) :
  nodes.append([*map(int, input().split())])

for i, p1 in enumerate(nodes) :
  x1, y1, x2, y2 = p1
  for ii, p2 in enumerate(nodes[i+1:]) :
    x3, y3, x4, y4 = p2
    if not cross(x1, y1, x2, y2, x3, y3, x4, y4) : continue
      
    union(roots, counts, i, ii + i+1)

print(roots.count(-1))
print(max(counts))