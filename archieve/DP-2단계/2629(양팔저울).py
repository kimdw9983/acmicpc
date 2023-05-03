nK = int(input())
K = [*map(int, input().split())]
nW = int(input())
W = [*map(int, input().split())]

MAX_WEIGHT = 40000
#MAX_WEIGHT = sum(W) #틀림
DP = [[False] * MAX_WEIGHT + [True] + [False] * MAX_WEIGHT]

for k in K :
  l = [False] * (MAX_WEIGHT * 2 + 1)
  for i, v in enumerate(DP[-1]) :
    if v :
      l[i-k] = l[i] = l[i+k] = True
  DP.append(l)

result = []
for w in W :
  if w > MAX_WEIGHT :
    result.append("N")
  else :
    result.append("Y" if DP[-1][w+MAX_WEIGHT] else "N")

print(" ".join(map(str, result)))