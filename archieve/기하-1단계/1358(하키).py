import math
W, H, X, Y, P = map(int, input().split())

cnt = 0
for _ in range(P) :
	nx, ny = map(int, input().split())
	r = H/2
	cnt = cnt+1 if (
	(X > nx and math.dist((X, Y+r), (nx, ny)) <= r) or 
	(X < nx and math.dist((X+W, Y+r), (nx, ny)) <= r) or 
	((X <= nx <= X+W) and (Y <= ny <= Y+H))
	) else cnt

print(cnt)