import sys, bisect
input = sys.stdin.readline
n = int(input())
DATA = tuple(map(int, input().split()))

l = [(-int(2e9), -1)]#입력 가장 작은 값보다 낮아야 한다.
for i, num in enumerate(DATA) :
	print(l)
	if l[-1][0] < num :
		l.append((num, -1))
	else :
		pos = bisect.bisect_left(l, num[0])
		x = l[pos]
		if x[1] == -1 :
			l[pos] = (num, i)
		else :
			l[pos] = (num, l[pos][1])


print(l)