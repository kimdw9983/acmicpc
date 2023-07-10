import sys
input = sys.stdin.readline
X = input().rstrip()
Y = input().rstrip()

def answer(X, Y) :
  DP = [0] * 1000

  for i, x in enumerate(X):
    cnt = 0
    for j, y in enumerate(Y):
      if cnt < DP[j]:
        cnt = DP[j]
      elif x == y:
        DP[j] = cnt + 1
  
  return max(DP)

print(answer(X, Y))

"""
ABKPCAB
BACABCA
"""