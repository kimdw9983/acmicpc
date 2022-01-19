import math
def eratosthenes(n):
	if n < 2: return []
	n += 1
	P = [1] * (n//2)
	for i in range(3, math.isqrt(n) + 1, 2):
		if P[i//2]: P[i**2//2::i] = [0]*((n-i**2-1)//(2*i) + 1)
	return [2] + [2*i+1 for i in range(1, n//2) if P[i]]

S = int(input())
l = eratosthenes(S)
s = e = x = cnt = 0
while True :
	if x >= S and s < e:
		x -= l[s]
		s += 1
	elif e == len(l) :
		break
	else :
		x += l[e]
		e += 1

	if x == S :
		cnt += 1
		
print(cnt)