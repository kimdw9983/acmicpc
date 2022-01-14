import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N	= int(input())
grid = list()

for i in range(N) :
		grid.append(input().split())

result = [0, 0, 0]
def paper(x, y, n) : #자르는것보다 어디부터 어디까지 탐색하게 하는지
		c = grid[x][y]
		for i in range(x, x + n):
				for j in range(y, y + n):
						if(grid[i][j] != c):
								for k in range(3):
										for l in range(3):
												paper(x + k * n//3, y + l * n//3, n//3)
								return
		
		result[int(c)+1] += 1

paper(0, 0, N)
print(*result, sep="\n")

"""
def split(grid) :
		n1 = len(grid) // 9
		n2 = n1 // 3

		for i in range(9) :
				if n1 == 1 :
						yield [grid[i]]
				else :
						start = n1*3*(i//3)+n2*(i%3)
						to = start + n2

						yield grid[start:to] + grid[start+n1:to+n1] + grid[start+n1*2: to+n1*2]

def papers(grid) :
		C = collections.Counter(grid)
		if len(C)-1 :
				for subgrid in split(grid) :
						paper(subgrid)
		else :
				result[int(list(C)[0])+1] += 1
"""
