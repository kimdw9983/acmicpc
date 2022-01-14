import sys
N = int(sys.stdin.readline())
l = [*map(int, sys.stdin.readline().split())]
l.sort()
for i in range(1, N) :
		l[i] = l[i-1] + l[i]
		
print(sum(l))