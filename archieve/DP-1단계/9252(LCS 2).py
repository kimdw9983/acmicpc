import sys
input = sys.stdin.readline
X = input().rstrip()
Y = input().rstrip()

def answer(X, Y) :
  DP = [""] * 1000
  l = ""
  for i, x in enumerate(X):
    s = ""
    for j, y in enumerate(Y):
      if len(s) < len(DP[j]):
        s = DP[j]
      elif x == y:
        con = s+x
        DP[j] = con
        l = con if len(l) < len(con) else l
      
  return l

ans = answer(X, Y)
print(len(ans))
if len(ans) :
  print(ans)