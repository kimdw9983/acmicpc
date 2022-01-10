N, B = input().split()

def numeric(c) :
	return int(c) if ord(c) < ord('A') else (ord(c)-55)

d10 = 0
for i, c in enumerate(N[::-1]) :
	d10 += int(B)**i * numeric(c)

print(d10)