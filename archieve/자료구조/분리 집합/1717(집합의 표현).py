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
	if A == B : return 

	if S[A] < S[B]: 
		S[B] = A
	elif S[A] > S[B]:
		S[A] = B
	else :
		S[A] -= 1
		S[B] = A

N, M = map(int,input().split())
S = [-1] * (N+1)
for _ in range(M):
	flag, a, b = map(int,input().split()) 
	if flag :
		sys.stdout.write(("YES" if find(S, a) == find(S, b) else "NO") + "\n")
	else :
		union(S, a, b)