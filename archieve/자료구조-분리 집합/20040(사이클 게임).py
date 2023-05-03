import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def upward(S, a, tmp) :
  s = S[a]
  if s < 0: 
    return a, tmp
  tmp.append(a)
  return upward(S, s, tmp)

def find(S, a): #루트 찾기
  f, x = upward(S, a, [])
  for n in x :
    S[n] = f
  return f

def union(S, a, b): #Union by Height
  A = find(S, a) 
  B = find(S, b) 
  if A == B : #사이클 발생
    global answer, i
    if answer == -1  :
      answer = i
    return 

  if S[A] < S[B]: 
    S[B] = A
  elif S[A] > S[B]:
    S[A] = B
  else :
    S[A] -= 1
    S[B] = A

N, M = map(int,input().split())
S = [-1] * N
answer = -1
for i in range(M):
  a, b = map(int,input().split()) 
  union(S, a, b)

print(answer+1)