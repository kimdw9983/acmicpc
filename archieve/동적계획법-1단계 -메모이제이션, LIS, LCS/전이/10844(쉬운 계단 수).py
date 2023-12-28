N = int(input())
memo = [[0] * 10 for _ in range(N)]
for i in range(9) :
  memo[0][i+1] = 1

for level, l in enumerate(memo) :
  for num in range(len(l)) :
    if num != 0 :
      l[num] = l[num] + memo[level-1][num-1]
    
    if num != 9 :
      l[num] = l[num] + memo[level-1][num+1]

if N == 1 :
  print(9)
else : 
  print(sum(memo[N-1]) % 1000000000)