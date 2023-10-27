"""
cnt = 1
X = n
while X :
  X -= math.isqrt(X)**2
  cnt += 1

print(cnt)
반례: 11339 = 106^2 + 10^2 + 1^2 + 1^2 + 1^2 = 
              105^2 + 15^2 + 8^2 + 5^2

import math
"""
n = int(input())

dp = [0, 1] + [0] * (n-1)
for i in range(n+1) :
  qrt = int(i**.5)#math.isqrt(i).. pypy에 없음..
  if i == qrt ** 2 :
    dp[i] = 1
  else :
    dp[i] = i
    for j in range(1, qrt+1) :
      dp[i] = min(dp[i], dp[i-j**2] + 1)

print(dp[n])