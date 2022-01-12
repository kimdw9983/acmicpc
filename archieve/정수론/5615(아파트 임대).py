import sys
input = sys.stdin.readline

def miller(n, a) : 
	if not a % n : return True
	k = n-1
	while True :
		tmp = pow(a,k,n)
		if tmp == n-1 : return True
		if k%2 : return tmp == 1 or tmp == n-1
		k //= 2

def is_prime32(a) : 
	if not a%2 : return False
	for n in (2,7,61) :
		if not miller(a, n) : return False
	return True

#2xy + x + y = (2x+1)(2y+1)
N = int(input())
cnt = 0
for _ in range(N) :
	x = int(input()) *2 + 1
	if is_prime32(x) :
		cnt += 1

print(cnt)