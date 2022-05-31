import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = 1
visited = [[False] * M for _ in range(N)]
root = [[0] * M for _ in range(N)]
grid = [input().rstrip() for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move = "UDLR"

def find(cnt, x, y):
	if not visited[x][y]:
		visited[x][y] = True
		i = move.index(grid[x][y]) #다음정점의 방향을 가져옴
		nx = x + dx[i]
		ny = y + dy[i]
		root[x][y] = find(cnt, nx, ny) #다음 정점을 찾음 + 사이클을 찾은경우 Z와 cnt중에 낮은 값으로 갱신

	#return min(cnt, root[x][y])
	Z = root[x][y]
	if Z < cnt and Z : 
		#print("lessor")
		return Z
	else :
		return cnt

for x, l in enumerate(visited) :
	for y, v in enumerate(l) :
		if not v :
			root[x][y] = cnt #root값을 정해줌
			res = find(cnt, x, y)
			cnt = cnt+1 if res == cnt else cnt

print(cnt-1)
#pprint(root)

"""
3 4
DLLL
DRLU
RRRU
4 4
DLLL
DDLU
DRUU
RRRU
4 4
DLLL
DDUU
DRUU
RRRU
4 6
DLLLLL
DUDUDU
DUDUDU
RRRRRU
4 6
RLLLLL
UUDUDU
ULLLLL
RRRRRU
10 10
DRDRRRRRRD
RDRUDUUUUL
URLDLRRRRD
RRRRLRDLUD
DDRLLDULUU
DRULLLRDUU
DULLDDDURU
URLDDDDUUL
DLRLRDUULL
RRULRUUURU
10 10
RRLLLLLRRL
UDDDULLDUU
RLURDULRUD
DULULLURRD
RUUURUDUDL
ULRUULLLLU
RDLLDDRLDD
DLRUULLRDL
UUUUUDULLD
URUULLRRRU
1 3
RRL
2 3
RRL
RRL
"""