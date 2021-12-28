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

    for i, v in enumerate(prime):
        if v:
            print(i)


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