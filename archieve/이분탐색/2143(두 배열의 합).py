import sys, itertools
input = sys.stdin.readline
T = int(input())

def IN() :
	input()
	S = [*map(int, input().split())]
	acc = [0]
	a = 0
	for v in S :
		a += v
		acc.append(a)
		
	l = dict()
	for s, e in itertools.combinations_with_replacement(range(len(S)), 2) :
		x = acc[e+1] - acc[s]
		if x in l :
			l[x] += 1
		else :
			l[x] = 1

	return l

A = IN()
B = IN()
answer = 0
for i, a in A.items() :
	if T-i in B :
		answer += a * B[T-i]

print(answer)