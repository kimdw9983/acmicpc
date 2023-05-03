import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
IN = [-1] + [0] * N #진입차수 갯수
for _ in range(M) :
  A, B = map(int, input().split())
  graph[A].append(B)
  IN[B] += 1

Q = []
dp = [0] * (N+1)
for i, e in enumerate(IN) :
  if not e :
    Q.append(i)

tmp = []
while Q :
  v = Q.pop()
  tmp.append(v)

  for e in graph[v] :
    IN[e] -= 1
    if not IN[e] :
      Q.append(e)
sys.stdout.write(" ".join(map(str, tmp)))

####################################################
#이게 더 빠른듯?
answer = []
for i in range(N) :
  v = Q.pop()
  answer.append(v)

  for e in graph[v] :
    IN[e] -= 1
    if not IN[e] :
      Q.append(e)

sys.stdout.write(" ".join(map(str, answer)))