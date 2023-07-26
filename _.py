DELTA = [90 / 2 ** i for i in range(1000)]
X, Y = input().split()

dx = dy = 0
if len(X) > 1 :
  for i, v in enumerate(X[1:], 1) :
    dx += DELTA[i] if v == X[0] else -DELTA[i]
      
if len(Y) > 1 :
  for i, v in enumerate(Y[1:], 1) :
    dy += DELTA[i] if v == Y[0] else -DELTA[i]

def tf(c) :
  if c == 'N' : return 0
  elif c == "E" : return 90
  elif c == "S" : return 180
  elif c == "W" : return 270

ans = tf(X[0]) + dx - (tf(Y[0]) + dy)
print(min(abs(ans), 360 - abs(ans)))