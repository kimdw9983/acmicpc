import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
IN = [-1] + [0] * N #진입차수 갯수
for _ in range(M) :
  l = [*map(int, input().split())]
  for i, v in enumerate(l[1:-1]) :
    A, B = v, l[i+2]
    graph[A].append(B)
    IN[B] += 1

Q = []
dp = [0] * (N+1)
for i, e in enumerate(IN) :
  if not e :
    Q.append(i)

answer = []
for i in range(N) :
  if not Q :
    answer = [0]
    break
  v = Q.pop()
  answer.append(v)

  for e in graph[v] :
    IN[e] -= 1
    if not IN[e] :
      Q.append(e)

sys.stdout.write("\n".join(map(str, answer)))