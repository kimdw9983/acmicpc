# CRT 성질을 이용해서 푸는 문제같다.

N, B = map(int, input().split())
memo = [[0] * B for _ in range(N)]
for i in range(B-1) :
  memo[0][i+1] = 1

for level, l in enumerate(memo) :
  for num in range(len(l)) :
    if num != 0 :
      l[num] = l[num] + memo[level-1][num-1]
    
    if num != B-1 :
      l[num] = l[num] + memo[level-1][num+1]

if N == 1 :
  print(B-1)
else : 
  print(sum(memo[N-1]) % 1000000000)

