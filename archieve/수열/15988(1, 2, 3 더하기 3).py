import sys
DP = [0, 0, 1] * 10000010
for i in range(2, 1000009) : #시발 몰라레후
		DP[i] = (DP[i-1] + DP[i-2]+ DP[i-3])%1000000009

N = int(sys.stdin.readline())
for T in range(N) :
	X = int(sys.stdin.readline())
	print(DP[X+2])