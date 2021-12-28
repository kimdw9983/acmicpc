X, Y = input(), input()
length = len(Y)
DP = [0] * length

for i in range(len(X)):
  cnt = 0
  for j in range(length):
    if cnt < DP[j]:
      cnt = DP[j]
    elif X[i] == Y[j]:
      DP[j] = cnt + 1

print(max(DP))
"""
ABKPCAB
BACABCA
"""