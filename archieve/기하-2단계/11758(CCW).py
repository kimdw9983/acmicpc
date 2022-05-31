l = [[*map(int, input().split())] for _ in range(3)]

R = l[0]
P = l[1]
Q = l[2]
#P의 x좌표에서 R의 x좌표를 빼서 원점에 맞춘다.
RxPy = (P[0] - R[0]) * (Q[1] - R[1])
RyPx = (P[1] - R[1]) * (Q[0] - R[0])
result = RxPy - RyPx

if result > 0 :
	print(1)
elif result < 0 :
	print(-1)
else :
	print(0)