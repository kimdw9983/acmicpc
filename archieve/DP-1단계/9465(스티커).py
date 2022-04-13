import sys
input = sys.stdin.readline
T = int(input())

def index(i, pos) : #pos가 -1이면 0과 1중에 큰거, 0이면1, 1이면 0
		return (0 if data[0][i] > data[1][i] else 1) if pos == -1 else 0 if pos else 1

def choose(a, b, i) :
		x = index(i, a[1])
		y = index(i, b[1])

		if a[0] + data[x][i] == b[0] + data[y][i] :
				return (a[0] + data[x][i], -1)
		else :
				return (a[0]+data[x][i], x) if (a[0] + data[x][i] > b[0] + data[y][i]) else (b[0] + data[y][i], y)

for _ in range(T) :
		N = int(input())
		dp = [[0] * 2 for i in range(N)]
		data = list()
		data.append([*map(int, input().split())])
		data.append([*map(int, input().split())])
		if N == 1 :
				print(max(data[1][0], data[0][0]))
		elif N == 2 :
				print(max(data[0][0] + data[1][1], data[1][0] + data[0][1]))
		else :
				dp[0][0] = (data[0][0], 0) #dp[n][위치] = (값, 위치)
				dp[0][1] = (data[1][0], 1)
				dp[1][0] = (data[0][0] + data[1][1], 1)
				dp[1][1] = (data[1][0] + data[0][1], 0)

				for i in range(2, N) :
						dp[i][0] = choose(dp[i-1][0], dp[i-2][0], i)
						dp[i][1] = choose(dp[i-1][1], dp[i-2][1], i)
								
				print(max(dp[-1])[0])
####################################################
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T) :
		N = int(input())
		dp = [[0] * 2 for i in range(N)]
		data = list()
		data.append([*map(int, input().split())])
		data.append([*map(int, input().split())])
		for j in range(1, N):
				if j == 1:
						data[0][j] += data[1][j - 1]
						data[1][j] += data[0][j - 1]
				else:
						data[0][j] += max(data[1][j - 1], data[1][j - 2])
						data[1][j] += max(data[0][j - 1], data[0][j - 2])
		print(max(data[0][N-1], data[1][N-1]))