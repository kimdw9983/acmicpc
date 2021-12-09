import sys
sys.setrecursionlimit(10**6)

PRICE = dict()
N = int(input())
for n in range(N) :
  for i, expense in enumerate(map(int, input().split())) : 
    PRICE[n, i] = expense

memo = dict()
for i in range(3) :
  memo[0, i] = PRICE[0, i]

def C(*key) :
  if key in memo :
    return memo[key]
  else :
    n, color = key
    if color == 0 :
      memo[key] = min(C(n-1, 1), C(n-1, 2)) + PRICE[key]
    elif color == 1 :
      memo[key] = min(C(n-1, 0), C(n-1, 2)) + PRICE[key]
    else :
      memo[key] = min(C(n-1, 1), C(n-1, 0)) + PRICE[key]

    return memo[key]

print(min(C(N-1, 0), C(N-1, 1), C(N-1, 2)))