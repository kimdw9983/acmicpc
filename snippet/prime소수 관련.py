
#쓸만한 소수
1234567891
1999
4447
5167
142857

#소수인지 판단(Trial division)
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


#밀러-라빈 소수 판정법, n이 10^6를 넘어갈 때 부터 사용한다.
#n이 '소수인것 같으면' true를 반환.
def miller(n, a) : 
  if not a % n : return True
  k = n-1
  while True :
    tmp = pow(a,k,n)
    if tmp == n-1 : return True
    if k%2 : return tmp == 1 or tmp == n-1
    k //= 2
#n < 4,759,123,141 일 경우 http://miller-rabin.appspot.com/
def is_prime32(a) : 
  for n in (2,7,61) :
    if not miller(a, n) : return False
  return True

#n < 2^64일 경우
def is_prime64(a) :
  result = True
  for n in (2, 325, 9375, 28178, 450775, 9780504, 1795265022) : #https://www.teferi.net/ps/%EC%86%8C%EC%88%98_%ED%8C%90%EB%B3%84
    result &= miller(a, n)
    if not result : break
  return result