#S = (ROOT노드 list)
#높이 list 없는 구현.
#단 x가 유일한 원소인 집합 S[x]의 내용물이 -1로 초기화 돼있어야만 가능.

def find(S, x):
  if S[x] < 0: return x
  S[x] = find(S, S[x])
  return S[x]

#union-by-height optimization
def union(S, a, b): 
  A = find(S, a)
  B = find(S, b)
  if A == B : return 

  if S[A] < S[B]:
    S[A] += S[B]
    S[B] = A
  else:
    S[B] += S[A]
    S[A] = B

#--------------------------------------------------------------------
#C = (높이 list)

def find(S, x) :
  if S[x] == x : return x
  S[x] = find(S, S[x])
  return S[x]

def union(S, a, b): 
  A = find(S, a)
  B = find(S, b)
  if A == B : return 

  if A < B :
    S[A] = B
  else :
    S[B] = A

#노드 갯수 구하기
def union(S, C, a, b):  
  A = find(S, a)
  B = find(S, b)
  if A == B : return

  S[B] = A
  C[A] += C[B]
  C[B] = 1

#union-by-height optimization
def union(S, C, a, b):  
  A = find(S, a)
  B = find(S, b)
  if A == B : return

  if C[A] < C[B]:
    S[A] = B
  else :
    S[B] = A
    if (C[A] == C[B]) : 
      C[A] += 1