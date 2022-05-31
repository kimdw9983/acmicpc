import sys, math
input = sys.stdin.readline

def include(x1, y1, x2, y2, d) :
	return math.dist([x1, y1], [x2, y2]) < d

def solve() :
	x1, y1, x2, y2 = map(int, input().split())

	n = int(input())
	cnt = 0
	for _ in range(n) :
		nx, ny, d = map(int, input().split())
		cnt = cnt + 1 if (include(x1, y1, nx, ny, d) and not include(x2, y2, nx, ny, d)) or (include(x2, y2, nx, ny, d) and not include(x1, y1, nx, ny, d)) else cnt

	print(cnt)
	
T = int(input())
for _ in range(T) : 
	solve()