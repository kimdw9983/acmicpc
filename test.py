import sys
input = sys.stdin.readline

def find(S, V, x) :
	V[x] = True
	if S[x] in (x, -1):
		return x
	S[x] = find(S, V, S[x])
	return S[x]

def union(S, V, a, b): 
	A = find(S, V, a)
	B = find(S, V, b)
	if A == B: return 

	if A < B :
		S[A] = B
	else :
		S[B] = A

while True :
	N, M = map(int, input().split())
	if N == M == 0 : break

	S = [*range(N+1)]
	visited = [False] * (N+1)
	for _ in range(M) :
		a, b = map(int, input().split())
		union(S, visited, a, b)
	
	result = set()
	for n in S :
		
		result.add(find(S, visited, n))
	pprint(S)
	print(result)