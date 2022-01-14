import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
PRICE = []
for i in range(N) :
	PRICE.append(tuple(map(int, input().split())))

memo = dict()
for i in range(3) :
  memo[0, i] = PRICE[0][i]

def C(*key) :
  if key in memo :
    return memo[key]
  else :
    n, color = key
    if color == 0 :
      memo[key] = min(C(n-1, 1), C(n-1, 2)) + PRICE[n][color]
    elif color == 1 :
      memo[key] = min(C(n-1, 0), C(n-1, 2)) + PRICE[n][color]
    else :
      memo[key] = min(C(n-1, 1), C(n-1, 0)) + PRICE[n][color]

    return memo[key]

print(min(C(N-1, 0), C(N-1, 1), C(N-1, 2)))