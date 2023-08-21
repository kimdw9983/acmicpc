import sys, itertools, math
input = sys.stdin.readline
TC = int(input())

def solve() :
  N = int(input())
  X = []
  Y = []
  for _ in range(N) :
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
  
  Xsum = sum(X)
  Ysum = sum(Y)
  answer = 9999999999
  for w in itertools.combinations(range(N), N//2) :
    endX_sum = endY_sum = 0
    for i in w : #더해야 하는 점들의 합
      endX_sum += X[i]
      endY_sum += Y[i]

    startX_sum = Xsum - endX_sum #시작합 = 전체합 - 끝합
    startY_sum = Ysum - endY_sum

    answer = min(answer, math.sqrt((endX_sum - startX_sum) ** 2 + (endY_sum - startY_sum) ** 2))

  print(answer)

for _ in range(TC) :
  solve()