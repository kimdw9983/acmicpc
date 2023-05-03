import sys
input = sys.stdin.readline
N, S = map(int, input().split())
l = [*map(int, input().split())]

s = e = x = 0
answer = 2**31-1
while True :
  if x >= S and s < e:
    x -= l[s]
    s += 1
  elif e == N :
    break
  else :
    x += l[e]
    e += 1
  
  if x >= S :
    answer = min(answer, e-s)

print(0 if answer == 2**31-1 else answer)