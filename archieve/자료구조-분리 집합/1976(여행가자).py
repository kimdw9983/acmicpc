import sys
input = sys.stdin.readline

def find(S, x) :
	if S[x] == x :
		return x
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

N = int(input())
M = int(input())
S = [*range(N+1)]
for x in range(N) :
	for y, v in enumerate(map(int, input().split())) :
		if not v : continue
		union(S, x+1, y+1)

result = set()
l = [*map(int, input().split())]
for c in l :
	result.add(find(S, c))

print("YES" if len(result) == 1 else "NO")