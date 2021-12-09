W = 8
H = 10
l = [[0] * W for _ in range(H)]

for w in l: #세로방향
  w#= [0, 0, 0, 0]
  for v in w : #값
    v#= 0


def has(l, *key) :
  try :
    l[key]
  except :
    return False
  return True