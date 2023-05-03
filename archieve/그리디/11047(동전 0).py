import sys
N, K = map(int, sys.stdin.readline().split())

l = list()
for T in range(N) :
  l.append(int(sys.stdin.readline()))

cnt = 0
while K :
  popped = l.pop()
  cnt += K//popped
  K %= popped

print(cnt)
"""
if len(l) == 1 :
  print(K)
else :
  cnt = 0
  while K : 
    for i in range(len(l)-1) :
      if K//l[i] and not K//l[i+1] :
        cnt += K//l[i]
        K %= l[i]
      elif i == len(l)-2 :
        cnt += K//l[i+1]
        K %= l[i+1]
  print(cnt)
"""