import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
for _ in range(N) :
  A.append([*map(int, input().split())])

M, K = map(int, input().split())
B = []  
for _ in range(M) :
  B.append([*map(int, input().split())])

C = [[0] * K for i in range(N)]
for i, l in enumerate(C) :
  for j, v in enumerate(l) :
    l[j] = sum([A[i][k] * B[k][j] for k in range(M)])
  sys.stdout.write(" ".join(map(str, l)) + "\n")
#########################################################
import sys
input = lambda: sys.stdin.readline().split()

N, M = map(int, input())
A = []
for _ in range(N) :
  A.append([*map(int, input())])

M, K = map(int, input())
B = []
for _ in range(M) :
  B.append([*map(int, input())])
B = list(zip(*B))

def calc(a, b) :
  res = 0
  for i, v in enumerate(a) :
    res += v * b[i]
  return res
  
for i in range(N) :
  for j in range(K) :
    sys.stdout.write(str(calc(A[i], B[j])) + " ")
  sys.stdout.write("\n")