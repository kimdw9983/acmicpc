#최대공약수
def gcd(m, n): 
    while n != 0:
        t = m % n
        (m, n) = (n, t)
    return abs(m)

#최소공배수
def lcm(m, n) :
    return m*n//gcd(m,n)

import math
math.factorial()
#팩토리얼

def divisors(n : int) : #n의 모든 약수 출력 O(n^.5)
    if not n :
        return [0]
    l = []
    for i in range(1, math.isqrt(n) + 1): 
        if not n % i:            
            l.append(i)
            l.append(n//i)
    return l[::2] + l[-3 if l[-1]==l[-2] else -1::-2]