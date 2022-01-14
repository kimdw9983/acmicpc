import sys
l = list()
l.append([])
l.append(["1"])
l.append(["11", "2"])
l.append(["111", "21", "12", "3"])

for i in range(4,10001) :
		s = set()
		for j in range(3, 0, -1) :
				for case in l[i-j] :
						for ci in range(len(case)+2) : 
								s.add(case[:ci]+ str(j) + case[ci:])
		l.append(list(s))

M, N = map(int, sys.stdin.readline().split())
if N > len(l[M]) :
		print(-1)
else :
		print("+".join(sorted(l[M])[N-1]))