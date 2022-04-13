n = int(input())
DATA = list(map(int, input().split()))
DP = [1] * n #최악의 경우 : 모든 수가 감소하는 수열일때

for i, num in enumerate(DATA) :
	for j in range(i) :
		if DATA[j] < num :
			DP[i] = max(DP[i], DP[j] + 1)

print(max(DP))