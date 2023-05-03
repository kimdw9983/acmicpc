import sys, collections
input = sys.stdin.readline

def find(S, x):
  if x not in S:
    return x
  S[x] = find(S, S[x])
  return S[x]

def union(S, C, a, b):  
  A = find(S, a)
  B = find(S, b)
  if A == B : return C[A]

  S[B] = A
  C[A] += C[B]
  C[B] = 1

  return C[A] #노드 갯수

TC = int(input())
def solve() :
  F = int(input())
  S = dict()
  C = collections.defaultdict(lambda : 1) #이름 : 친구 수
  result = []
  for _ in range(F) :
    a, b = input().split()
    result.append(union(S, C, a, b))
  print("\n".join(map(str, result)))
  
for _ in range(TC) :
  solve()