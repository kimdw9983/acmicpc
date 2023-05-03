import sys
command = [*map(int, sys.stdin.readline().split()[:-1])]

def step(s,e) :
  e = int(e)
  if not s-e : return 1
  elif not s : return 2
  elif (s+2) % 4 == e : return 4 
  return 3

def solve() : 
  #틀린 풀이: 이 방법은 왼쪽밟았을때와 오른쪽 밟았을때의 경우를 확인하는 greedy였다. L=R일때 더 많은 경우의 수로 갈라져야 하는데, 그러지 못해서 반례가 발생했다.
  dp = dict()
  dp[0, 0, 0] = 0
  Ll = Lr = Rl = Rr = 0
  
  for i, v in enumerate(command) :
    B = 0
    L = dp[i, Ll, Lr] + step(Ll, v)#이전에 왼쪽을 밟고, 왼쪽을 갱신
    R = dp[i, Rl, Rr] + step(Rl, v)#이전에 오른쪽을 밟고, 왼쪽을 갱신
    
    if L <= R :
      dp[i+1, v, Lr] = L
    else :
      B |= 1
      dp[i+1, v, Rr] = R

    L = dp[i, Ll, Lr] + step(Lr, v)#이전에 왼쪽을 밟고, 오른쪽을 갱신
    R = dp[i, Rl, Rr] + step(Rr, v)#이전에 오른쪽을 밟고, 오른쪽을 갱신

    if L <= R :
      dp[i+1, Ll, v] = L
      B |= 2
    else :
      dp[i+1, Rl, v] = R
    
    if B&1 :
      Lr = Rr
    if B&2 :
      Rl = Ll

    Ll = v
    Rr = v
  
  return min(dp[i+1, Ll, Lr], dp[i+1, Rl, Rr])

print(solve())
##################################################
#..그런줄 알앗는데 L=R때문이 아니였다. 
#깊이가 깊어질때마다 고려해야 하는 경우가 있는데, 
#짰었던 코드로는 깊이가 1번밖에 깊어질 수 없었다.
def DDR() :
  for i, c in enumerate(command) :
    for l in range(5) :
      for r in range(5) :
        if dp[i, l, r] != 1234567891 :
          x = dp[i, l, r]
          L = step(l, c)
          R = step(r, c)
          if x + L < x + R :
            dp[i+1, c, r] = x + L
          elif x + R < x + L :
            dp[i+1, l, c] = x + R
          else :
            dp[i+1, c, r] = x + L
            dp[i+1, l, c] = x + R

  return 

#########################################################3
#(s-e) % 4 = 3
N = len(command)
def DDR(i, l, r) :
  if i == N : 
    return 0
  if dp[i, l, r] != 1234567891 :
    return dp[i, l, r]
  
  c = command[i]
  L = step(l, c) + DDR(i+1, c, r)
  R = step(r, c) + DDR(i+1, l, c)
  
  dp[i, l, r] = min(L, R)
  return dp[i, l, r]
  
dp = memo()
print(DDR(0, 0, 0))
###################################################333
import sys, collections
sys.setrecursionlimit(10**6)
command = [*map(int, sys.stdin.readline().split()[:-1])]

def step(s,e) :
  e = int(e)
  if not s-e : return 1
  elif not s : return 2
  elif (s-e) % 4 == 2 : return 4 
  return 3

dp = collections.defaultdict(lambda: 1234567891)
N = len(command)
def DDR(i, l, r) :
  if i == N : return 0
  if (i, l, r) in dp : return dp[i, l, r]
  
  c = command[i]
  L = step(l, c) + DDR(i+1, c, r)
  R = step(r, c) + DDR(i+1, l, c)
  
  dp[i, l, r] = min(L, R)
  return dp[i, l, r]
  
print(DDR(0, 0, 0))