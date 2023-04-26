grid = [[1,2], [2,3], [3,4], [1,4], [1,0], [2,1]]
#2차원 배열 키 한개 기준 정렬
sorted(grid, key = lambda x: x[0])

#x[0]은 오름차순, x[1]은 내림차순으로 정렬
sorted(grid, key=lambda x: (x[0], -x[1]))
grid[0] #x[0]이 가장 낮고, x[1]이 가장 높음