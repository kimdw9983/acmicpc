import sys
input = sys.stdin.readline
N = int(input())
l = [0] + [*map(int, input().split())]
dp = [[]] + [[0] + [0] *(i-1) + [1] + [-1] * (N-i) for i in range(1, N+1)]

def C(s, e) : #펠린드롬??????
  if dp[s][e] != -1 :
    return dp[s][e]
  
  if s+1 == e  : #2개의 연속된숫자가 같으면
    result = 1 if l[s] == l[e] else 0
    dp[s][e] = result
    return result

  if l[s] == l[e] :
    result = C(s+1, e-1)
    dp[s][e] = result  
    return result
  else : 
    dp[s][e] = 0
    return 0

M = int(input())
answer = []
for _ in range(M) :
  S, E = map(int, input().split())
  answer.append(C(S, E))

print("\n".join(map(str, answer)))