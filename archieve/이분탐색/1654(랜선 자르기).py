import sys
K, N = map(int, sys.stdin.readline().split())
DATA = [0] * K

for i in range(K) :
	DATA[i] = int(sys.stdin.readline())

def decision(Z): #결정 함수
	cnt = 0
	for a in DATA :
		x = a//Z
		cnt += x
		if cnt >= N : #충분한 갯수를 모은 경우 
			return True
	#충분히 갯수를 모으지 못한 경우

low = 0
high = 2**31
while low + 1 < high:
	mid = (low + high) // 2
	if decision(mid):
		low = mid
	else:
		high = mid

print(low)