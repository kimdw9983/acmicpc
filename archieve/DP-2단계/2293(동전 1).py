import sys
input = sys.stdin.readline

n, k = map(int, input().split())

C = []
for _ in range(n) :
	C.append(int(input()))

DP = [1] + [0] * k
for c in C :
	for i, v in enumerate(DP) :
		if i < c : continue
		if i-c < 0 : continue
		DP[i] += DP[i-c]

print(DP[k])