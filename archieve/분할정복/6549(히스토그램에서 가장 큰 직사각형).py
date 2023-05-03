import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

answer = []
while True :
  l = [*map(int, input().split())]
  if l == [0] :
    break
  l = l[1:] #아 구라치지 마셈
  
  def getArea(s, e, m) :
    left = right = m
    height = l[m] #가장 큰 직사각형 룰을 맞추기 위해(더 낮은 높이로 갱신하기 위해) 사용하는 변수
    area = height #초기값은 너비가 1이므로
    
    def toLeft() : 
      nonlocal left, right, height, area
      left -= 1
      height = min(height, l[left])
      area = max(area, height * (right - left + 1))

    def toRight() :
      nonlocal left, right, height, area
      right += 1
      height = min(height, l[right])
      area = max(area, height * (right - left + 1))
    
    while s < left and e > right:
      if l[left-1] > l[right+1] : 
        toLeft()
      else :
        toRight()

    while e > right :
      toRight()

    while s < left :
      toLeft()

    return area
  
  def R(s, e) :
    if s == e : return l[s]

    m = (s+e)//2
    big = max(R(s, m), R(m+1, e)) #인접한 (계산된)구간의 넓이 중에서 더 큰 구간의 넓이
    return max(big, getArea(s, e, m)) #현재 구간의 넓이와 인접한것중에 더 큰걸로 갱신해서 반환 
  
  answer.append(R(0, len(l)-1))

print("\n".join(map(str, answer)))