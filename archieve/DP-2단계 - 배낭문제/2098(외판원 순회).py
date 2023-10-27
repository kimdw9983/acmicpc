import sys, collections
input = sys.stdin.readline
N = int(input())
w = [[*map(int, input().split())] for _ in range(N)]

FULL = (1 << N) - 1
INF = int(3e9)
dp = collections.defaultdict(lambda: 2147483647)
def TSP(x, check):
  if (check == FULL) : #다 순회했으면,
    if not w[x][0] : return INF
    return w[x][0]
  
  if (x, check) in dp : return dp[x, check]

  for i in range(N) :
    to = check | (1<<i) #i도시 방문
    #경로가 없거나, 도시를 이미 방문한 경우
    if not w[x][i] or (check & (1 << i) != 0) : continue
    
    dp[x, check] = min(dp[x, check], TSP(i, to) + w[x][i])
  
  return dp[x, check]

print(TSP(0, 1))
#######################################################3
import sys
input = sys.stdin.readline
N = int(input())
w = [[*map(int, input().split())] for _ in range(N)]

FULL = (1 << N) - 1
INF = int(3e9)
dp = [[INF] * FULL for _ in range(N)]
def TSP(x, check):
  if (check == FULL) : #다 순회했으면,
    if not w[x][0] : return INF
    return w[x][0]
  
  if dp[x][check] != INF : return dp[x][check]

  for i in range(N) :
    to = check | (1<<i) #i도시 방문
    #경로가 없거나, 도시를 이미 방문한 경우
    if not w[x][i] or (check & (1 << i) != 0) : continue
    
    dp[x][check] = min(dp[x][check], TSP(i, to) + w[x][i])
  return dp[x][check]

print(TSP(0, 1))