import itertools
N, S = map(int, input().split())
L = [*map(int, input().split())]

def calc(l) :
	d = dict()
	
	for c in itertools.chain.from_iterable(itertools.combinations(l, r+1) for r in range(N)) :
			x = sum(c)
			if x in d : 
				d[x] += 1
			else :
				d[x] = 1

	return d

A = calc(L[:N//2]); B = calc(L[N//2:])
answer = 0
for k, v in A.items() :
	if S-k in B:
		answer += B[S-k] * v
	if k == S :
		answer += v
if S in B :
	answer += B[S]

print(answer)