MAX_SIZE = 10000
DATA = [0] * (MAX_SIZE+1)
DP = [0] * (MAX_SIZE+1)

n = int(input())
for i in range(n):
  DATA[i] = int(input())

DP[0] = DATA[0]
DP[1] = DATA[0] + DATA[1]
DP[2] = max(DATA[1] + DATA[0], DATA[0] + DATA[2], DATA[1] + DATA[2])

for i in range(3, n):
  DP[i] = max(DP[i-3] + DATA[i-1] + DATA[i], DP[i-2] + DATA[i], DP[i-1])

print(DP[n-1])