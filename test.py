N = int(input())

for T in range(N) :
  _, M = map(int, input().split())
  L = list()
  for i in [*map(int, input().split())][::-1] :
    L.append(i)
  print(L)
  
  D = sorted([*enumerate(L)], key = lambda x: x[1], reverse=True)
  print(D, M)

  for i, v in enumerate(D) :
    if v[0] == M :
      print(i)