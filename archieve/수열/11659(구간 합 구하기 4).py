import sys
input=sys.stdin.readline
M, N = map(int, input().split())
l = [0] + [0] * M

n = ""
i = 1
for c in input() : #개행문자 제거
		if c == " " :
				l[i] = l[i-1] + int(n)
				i += 1
				n = ""
		else :
				n += c
l[i] = l[i-1] + int(n)

for i in range(N) :
		X, Y = map(int, input().split())
		sys.stdout.write(str(l[Y] - l[X-1])+"\n")