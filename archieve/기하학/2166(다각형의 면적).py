import sys
input = sys.stdin.readline
N = int(input())

X = []; Y = []
for i in range(N) :
	x, y = map(int, input().split())
	X.append(x)
	Y.append(y)
X += [X[0]]
Y += [Y[0]]

x = y = 0
for i in range(N) :
	x += X[i] * Y[i+1]
	y += Y[i] * X[i+1]

print(round(abs(x-y)/2, 1)) #소수 둘째 자리에서 반올림