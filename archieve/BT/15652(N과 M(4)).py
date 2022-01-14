N,M = map(int, input().split())
l = []

def BT(level, num) :
	if level-1 == M :
		print(' '.join(map(str, l)))
		return
	
	for i in range(num, N+1) :
		l.append(i)
		BT(level+1, i)
		l.pop()
BT(1,1)