import sys
sys.setrecursionlimit(10**6)
IT = dict() #Integer Triangle

N = int(input())
for n in range(N) :
  for i, v in enumerate(map(int, input().split())) : 
    IT[n, i] = v

memo = dict()
memo[0,0] = IT[0,0]
 
def DP(*key) :
  if key in memo :
    return memo[key]
  else :
    a, b = key
    if b == 0 : #왼쪽 위 경로를 선택할 수 없는 경우
      memo[key] = DP(a-1, 0) + IT[key]
    elif b >= a : #오른쪽 위 경로를 선택할 수 없는 경우
      memo[key] = DP(a-1, b-1) + IT[key]
    else :
      memo[key] = max(DP(a-1, b), DP(a-1, b-1)) + IT[key]

    return memo[key]

solution = list()
for i in range(N) :
  solution.append(DP(N-1, i))

print(max(solution))