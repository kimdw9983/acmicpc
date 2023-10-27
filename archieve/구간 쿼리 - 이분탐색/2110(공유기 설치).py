import sys, bisect
input = sys.stdin.readline
N, C = map(int, input().split())

l = sorted([int(input()) for _ in range(N)])

#Z: 인접할 공유기 사이의 최소 거리 + 매개 변수
def decision(Z) :
  tmp = l[0]
  for i in range(C-1) :
    tmp += Z
    index = bisect.bisect_left(l, tmp)
    if index >= len(l) : 
      return False
    else :
      tmp = l[index]
  return True
  
low = 1
high = l[-1]
while low <= high:
  mid = (low + high) // 2
  if decision(mid):
    answer = mid
    low = mid + 1
  else:
    high = mid - 1
print(answer)