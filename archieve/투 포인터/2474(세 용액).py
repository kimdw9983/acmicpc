import sys
input = sys.stdin.readline
N =	int(input())
L = sorted([*map(int, input().split())])

x = 2**64+1 #절댓값 최소
S = L[0]
E = L[1]
I = L[2]
for _i in range(N-2) :
	i = N-_i-1
	Z = L[i]
	s = 0
	e = i-1
	while s < e :
		mix = L[s] + L[e] + Z
		if x > abs(mix) :
			x = abs(mix)
			S = L[s]
			E = L[e]
			I = Z

		if mix > 0 :
			e -= 1
		elif mix < 0 :
			s += 1
		else :
			break

print(S, E, I)