n = int(input())
DATA = list(map(int, input().split()))
DP = [1] * n

for i, num in enumerate(DATA) :
	for j in range(i) :
		if DATA[j] < num :
			DP[i] = max(DP[i], DP[j] + 1)

DP2 = [1] * n
for i in range(n-1, -1, -1) :
	for j in range(n-1, i, -1) :
		if DATA[i] > DATA[j] :
			DP2[i] = max(DP2[i], DP2[j] + 1)

result = 0
for i in range(n) :
	result = max(result, DP[i] + DP2[i])

print(result - 1)