import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def union(S, a, b):
	A = find(S, a)
	B = find(S, b)
	if A == B : return 
	
	if S[B] < S[B]:
		S[A] += S[B]
		S[B] = A
	else:
		S[B] += S[A]
		S[A] = B

def find(S, x):
	if S[x] < 0:
		return x
	S[x] = find(S, S[x])
	return S[x]