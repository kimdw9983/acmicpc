import sys 
sys.setrecursionlimit(10**6) 

def paint_star(LEN): 
	DIV3 = LEN//3 
	if LEN == 3: 
		g[1] = ['*', ' ', '*'] 
		g[0][:3] = g[2][:3] = ['*']*3 
		return 
		
	paint_star(DIV3) 
	
	for i in range(0, LEN, DIV3): 
		for j in range(0, LEN, DIV3): 
			if i != DIV3 or j != DIV3: 
				for k in range(DIV3): 
					g[i+k][j:j+DIV3] = g[k][:DIV3] 
								
n = int(input().strip()) 
g = [[' ' for _ in range(n)] for _ in range(n)]
paint_star(n) 

for i in range(n): 
	for j in range(n): 
		print(g[i][j], end='') 
	print()

####################################################
n= int(input())

def concat(r1, r2):
	return [''.join(x) for x in zip(r1, r2, r1)]

def star(n):
	if n == 1:
		return ['*']
	n //= 3
	x = star(n)
	top_bottom = concat(x, x) 
	middle = concat(x, [' ' * n] * n)
	return top_bottom + middle + top_bottom

print('\n'.join(star(n)))