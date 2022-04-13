import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
PRICE = []
for _ in range(N) :
	PRICE.append(tuple(map(int, input().split())))

memo = dict()
HUGE = int(2e9)
def init(j) : #시작 색깔을 j번째만 고르도록 memo를 초기화
	global memo
	memo = dict()
	memo[0, j] = PRICE[0][j]
	memo[0, (j+1)%3] = HUGE
	memo[0, (j+2)%3] = HUGE

def C(n, c) :
	if (n,c) in memo :
		return memo[n,c]
	else :
		memo[n,c] = min(C(n-1, (c+1)%3), C(n-1, (c+2)%3)) + PRICE[n][c]

		return memo[n,c]

answer = HUGE
for i in range(3) :
	init((i+1)% 3)
	answer = min(answer, C(N-1, i))
	
	init((i+2)% 3)
	answer = min(answer, C(N-1, i))

print(answer)