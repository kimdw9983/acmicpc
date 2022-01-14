import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N	= int(input())
num_blue = num_white = 0

grid = list()
for i in range(N) :
		grid.append([*map(int, input().split())])

def merged(grid) :
		merged = list()
		for l in grid : 
				merged += l
		return merged

def split(grid) :
		n = len(grid) // 2
		g1=list(); g2=list(); g3=list(); g4=list()
		for i in range(n*2) :
				if i < n :
						g1.append(grid[i][:n])
						g2.append(grid[i][n:])
				else :
						g3.append(grid[i][:n])
						g4.append(grid[i][n:])
		
		yield g1
		yield g2
		yield g3
		yield g4

def paper(grid) :
		global num_blue, num_white
		s = set(merged(grid))
		if len(s) == 1 : #단색으로 구성된 경우
				if list(s)[0] : #파란색이면
						num_blue += 1
				else :
						num_white += 1
		else :
				for subgrid in split(grid) :
						paper(subgrid)

paper(grid)
print(num_white, num_blue)