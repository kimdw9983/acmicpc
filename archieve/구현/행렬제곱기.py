import sys
input = lambda: sys.stdin.readline().split()

N = map(int, input())
A = []
for _ in range(N) :
	A.append([*map(int, input())])

A_ = list(zip(*A))
def calc(a, j) :
	res = 0
	for i, v in enumerate(a) :
		res += v * A_[j][i]
	return res
	
for i in range(N) :
	for j in range(N) :
		sys.stdout.write(str(calc(A[i], j)) + " ")
	sys.stdout.write("\n")