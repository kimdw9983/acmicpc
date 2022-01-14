import sys
K, N = map(int, sys.stdin.readline().split())
DATA = [*map(int, sys.stdin.readline().split())]

def decision(Z): #결정 함수
	sum = 0
	for a in DATA :
		if a < Z :
			continue
		x = a-Z
		sum += x
		if sum >= N :
			return True

low = 0
high = 1000000001
while low + 1 < high:
	mid = (low + high) // 2
	if decision(mid):
		low = mid
	else:
		high = mid

print(low)