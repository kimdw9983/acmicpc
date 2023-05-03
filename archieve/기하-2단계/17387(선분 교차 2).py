x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def CCW(ax, ay, bx, by, cx, cy) :
  ccw = (bx-ax) * (cy-ay) - (cx-ax) * (by-ay)

  if ccw > 0 : return 1
  elif ccw < 0 : return -1
  return 0

A = CCW(x1, y1, x2, y2, x3, y3) * CCW(x1, y1, x2, y2, x4, y4) 
B = CCW(x3, y3, x4, y4, x1, y1) * CCW(x3, y3, x4, y4, x2, y2)

def swap(A, B) :
  A, B = sorted([A, B], key= lambda x: (x[0], x[1]))
  return *A, *B

def compare(ax, ay, bx, by) :
  if ax == bx :  return ay <= by
  else : return ax <= bx 
  
if A == B == 0 : #4점 한직선
  x1, y1, x2, y2 = swap((x1, y1), (x2, y2))
  x3, y3, x4, y4 = swap((x3, y3), (x4, y4))

  print(1 if compare(x3, y3, x2, y2) and compare(x1, y1, x4, y4) else 0)
elif A == 0 or B == 0 : #3점 한직선
  print(1 if A <= 0 and B <= 0 else 0)
elif A < 0 and B < 0 : #교차하는 경우
  print(1)
else :
  print(0)