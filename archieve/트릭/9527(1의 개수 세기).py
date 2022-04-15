import math

def A001787(x) : #[0 ~ 2^x-1] 구간 사이의 '1'의 갯수 총합
	return int(x * 2 ** (x-1))

def sum(x) : #[0~x] 구간 사이의 '1'의 갯수 총합
	l = 1 if x <= 1 else int(math.log2(x))+1 
	cnt = answer = 0
	
	for i in range(l+1) :
		n = 1 << (l-i)
		if x&n :
			answer += cnt * n + A001787(l-i)
			cnt += 1
	answer += bin(x)[2:].count('1')
	return answer
	
A, B = map(int,input().split())
print(sum(B) - sum(A-1))