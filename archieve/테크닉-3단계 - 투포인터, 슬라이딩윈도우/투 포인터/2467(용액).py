import sys
input = sys.stdin.readline
N =  int(input())
L = [*map(int, input().split())]

if L[0] > 0 :
  #전부 양수인 경우
  pass
else :
  for i, v in enumerate(L[:-1]) : 
    #음수->양수로 가는 경계점 찾기(O(n))
    if v < 0 and L[i+1] > 0 :
      break
  s = i
  e = s+1
  x = int(1e9) + 1 #절댓값 최소
  while True :
    S = L[s]
    E = L[e]
    x = min(x, abs(S+E))

    if abs(E) < abs(S) :
      if e == N-1 :
        break
      else :
        e += 1
    else :
      if s == 0 :
        break
      else :
        s -= 1
  
  print(L[s],L[e],x)
  #반례 : 예제 입력 2
  #(중앙부터 퍼지면 한쪽으로 치우쳐진 경우를 잡지 못한다.)

  
import sys
input = sys.stdin.readline
N =  int(input())
L = sorted([*map(int, input().split())])

s = 0 
e = N-1
x = 2**31+1 #절댓값 최소
S = L[0]
E = L[1]

while s < e :
  mix = L[s] + L[e]
  if x > abs(mix) :
    x = abs(mix)
    S = L[s]
    E = L[e]

  if mix > 0 :
    e -= 1
  elif mix < 0 :
    s += 1
  else :
    break

print(S, E)