import sys, collections
input = sys.stdin.readline
N, M = map(int, input().split())
L = collections.defaultdict(lambda: -1)

acc = 0
for x in map(int, [0] + [*input().split()]) :
	acc += x
	L[acc % M] += 1


memo = dict()
result = 0
for v in L.values() : 
	if v in memo :
		result += memo[v]
	else :
		memo[v] = sum(range(1, v+1))
		result += memo[v]
	result += sum(range(1, v+1))

print(result)

####################정답함수
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
L = [*map(int, input().split())]

acc = 0
for l in range(N) :
	for r in range(N) :
		sum = 0
		for z in range(l, r+1) :
			sum += L[z]

#		print(sum)
		if not sum % M and sum :
			print(l+1, r+1, sum)
			acc = acc + 1

print("\n", acc)