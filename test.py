import sys, collections
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N  = int(input())
grid = list()

for i in range(N) :
    grid += input().split()

def split(grid) :
    n = len(grid) // 9

    for i in range(9) :
        yield grid[n*i:n*i+n//3]

result = [0, 0, 0]
def paper(grid) :
    C = collections.Counter(grid)
    if len(C)-1 :
        for subgrid in split(grid) :
            paper(subgrid)
    else :
        result[int(list(C)[0])+1] += 1
        #C = C.most_common(1)[0]
        #result[int(C[0])+1] += C[1]

paper(grid)
print(*result, sep="\n")