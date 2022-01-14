import sys
M, N = map(int, sys.stdin.readline().split())

def z(num) :
	return sum(num//5**i for i in range(1,15))#5^14 > 20억
def v(num) :
	return sum(num//2**i for i in range(1, 33))

print(min(z(M)-z(N)-z(M-N), v(M)-v(N)-v(M-N)))