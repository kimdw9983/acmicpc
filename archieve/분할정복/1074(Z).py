N, r, c = map(int, input().split())

l = [[0] * 2**N for n in range(2**N)] 
cnt = 0
def Z(x, y, n) :
		global cnt
		if n == 1 :
				l[x][y] = cnt
				l[x][y+1] = cnt+1
				l[x+1][y] = cnt+2
				l[x+1][y+1] = cnt+3
				cnt += 4
		else :
				DIV = 2**n//2
				Z(x, y, n-1)
				Z(x, y+DIV, n-1)
				Z(x+DIV, y, n-1)
				Z(x+DIV, y+DIV, n-1)

Z(0, 0, N)
#print(*l, sep="\n")
print(l[r][c])
###########################################################
import sys
N, r, c = map(int, sys.stdin.readline().split())

num = 0
while True :
		if r < 2 and c < 2 :
				num += r*2 + c
				break
		
		#p2r = int(math.log2(r)) #log2(x) x는 0보다 커야함.
		p2r = r.bit_length() - 1
		p2c = c.bit_length() - 1
		
		if not p2r - p2c : #p2r == p2c
				num += 4**p2r * 3
				r -= 2**p2r
				c -= 2**p2c
		elif p2r > p2c : 
				num += 4**p2r * 2 
				r -= 2**p2r
		else :
				num += 4**p2c
				c -= 2**p2c
		
print(num)