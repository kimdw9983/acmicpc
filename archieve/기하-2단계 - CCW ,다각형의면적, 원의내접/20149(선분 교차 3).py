x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def CCW(ax, ay, bx, by, cx, cy) :
  cp = (bx-ax)*(cy-ay) - (cx-ax)*(by-ay) #벡터의 외적

  if cp > 0 : return 1
  if cp < 0 : return -1
  return 0

def swap(A, B) :
  A, B = sorted([A, B], key= lambda x: (x[0], x[1]))
  return *A, *B

def cmp(ax, ay, bx, by) :
  if ax == bx :  return ay <= by
  else : return ax <= bx 

A1 = CCW(x1, y1, x2, y2, x3, y3)
A2 = CCW(x1, y1, x2, y2, x4, y4) 
B1 = CCW(x3, y3, x4, y4, x1, y1)
B2 = CCW(x3, y3, x4, y4, x2, y2)
A = A1 * A2
B = B1 * B2
#print(A1, A2, B1, B2)

if A == B == 0 :
  _x1, _y1, _x2, _y2 = swap((x1, y1), (x2, y2))
  _x3, _y3, _x4, _y4 = swap((x3, y3), (x4, y4))

  if cmp(_x3, _y3, _x2, _y2) and cmp(_x1, _y1, _x4, _y4) : #1 - 4 사이 공간에 2, 3의 위치 관계를 통해 교점 여부를 파악한다.
    print(1)

    #한 점 이상 만난다.
    #무수히 많은 점을 지날 경우 출력하지 않는다.
    if ((A1 * B2) == 0 and A2 != 0) or ((A2 * B1) == 0 and A1 != 0) :
      #print(A1, A2, B1, B2)
      if (x1, y1) == (x3, y3) or (x1, y1) == (x4, y4):
        print(x1, y1)
      elif (x2, y2) == (x3, y3) or (x2, y2) == (x4, y4): 
        print(x2, y2)
      else : 
        print("????")
    elif _x2 == _x3 and _y2 == _y3 :
      #print("p2p3")
      print(float(_x2), float(_y2))
    elif _x1 == _x4 and _y1 == _y4 :
      #print("this")
      print(float(_x1), float(_y1))
  else: 
    print(0)
elif A <= 0 and B <= 0 : #둘다 부호가 서로 다를 경우
  print(1)
  print( ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / ((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)), ((x1*y2 - y1*x2)*(y3-y4) - (y1 - y2)*(x3*y4 - y3*x4)) / ((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)) )
else :
  print(0)