#최대공약수 (기약분수)
#python 3.9버전 이후로부터는 gcd(*arg) 가 됐음.
import math
math.gcd()


#최소공배수
import math
def lcm(m, n) :
		return m*n//math.gcd(m,n)


#팩토리얼
import math
math.factorial()


#n의 모든 약수 출력 O(n^.5)
def divisors(n : int) :
	if not n :
		return [0]
	l = []
	for i in range(1, math.isqrt(n) + 1): 
		if not n % i:						
			l.append(i)
			l.append(n//i)
	return l[::2] + l[-3 if l[-1]==l[-2] else -1::-2]


#소수인지 판단
#https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
import math
def is_prime(n):
	if n == 2 or n == 3: return True
	if n < 2 or n % 2 == 0: return False
	if n < 9: return True
	if n % 3 == 0: return False
	r = math.isqrt(n)
	f = 5
	while f <= r:
		if n % f == 0: return False
		if n % (f + 2) == 0: return False
		f += 6
	return True


#에라토스테네스의 체
#https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
def eratosthenes(n):
	prime = [False] * 2 + [True for i in range(n - 1)]
	p = 2
	while (p * p <= n):
		if prime[p]:
			for i in range(p**2, n + 1, p):
				prime[i] = False
		p += 1

	return prime
#숫자list로 출력
import math
def eratosthenes_2(n):
	if n < 2: return []
	n += 1
	P = [1] * (n//2)
	for i in range(3, math.isqrt(n) + 1, 2):
		if P[i//2]: P[i**2//2::i] = [0]*((n-i**2-1)//(2*i) + 1)
	return [2] + [2*i+1 for i in range(1, n//2) if P[i]]

#이항 계수(binomial coefficient)
def bin(n, k):
	if (k > n//2) : #이항계수의 성질
		k = n-k
	B = [0] * (k+1)
	B[0] = 1
	for i in range(1, n+1):
		j = min(i, k)
		while (j > 0):
			B[j] = B[j] + B[j-1]
			j -= 1
	return B[k]


#A^B%C를 효율적으로 처리.
pow(a,b,c)


#분할 정복을 이용한 거듭제곱
dp = [0000] #초기값 넣기
B = 1234
for b in range(B.bit_length()) : #b = bit
	x = dp[-1]
	dp.append(x * x) #제곱한걸 넣는다
	if B&(1<<b) : 
		pass
B % 1234567891 #대충 마무리 작업


#쓸만한 소수
1234567891
1999
4447
5167
142857


#밀러-라빈 소수 판정법
#n이 '소수인것 같으면' true를 반환.
def miller(n, a) : 
	if not a % n : return True
	k = n-1
	while True :
		tmp = pow(a,k,n)
		if tmp == n-1 : return True
		if k%2 : return tmp == 1 or tmp == n-1
		k //= 2
#n < 4,759,123,141 일 경우
def is_prime32(a) : 
	for n in (2,7,61) :
		if not miller(a, n) : return False
	return True

#n < 2^64(출처 몰?루) 일 경우
def is_prime64(a) :
	result = True
	for n in (2,3,5,7,11,13,17,19,23,29,31,37) :
		result &= miller(a, n)
		if not result : break
	return result

#자릿수
import math
math.log10