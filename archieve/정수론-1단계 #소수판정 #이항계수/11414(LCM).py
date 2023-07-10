A, B = map(int, input().split())
def gcd(m, n): 
    while n != 0:
        t = m % n
        (m, n) = (n, t)
    return abs(m)

#최소공배수
def lcm(m, n) :
    return m*n//gcd(m,n)

N = 0
THRESHOLD = 100000
A, B = sorted((A, B))
l = list()
while True :
    if N > THRESHOLD :
        break
    
    l.append(lcm(A+N, B+N))
    N += 1

print(A, B)
l = sorted(enumerate(l), key= lambda x: x[1])
for i in range(15) :
    print(f"{l[i]}, A = {A+l[i][0]}, B = {B+l[i][0]}")

#정답의 패턴을 구하기 위해 찾은 함수
############################################################
import math
def lcm(m, n) :
    return m*n//math.gcd(m,n)

def divisors(n : int) :
    if not n:
        return [1]
    l = []
    for i in range(1, math.isqrt(n) + 1): 
        if not n % i:            
            l.append(i)
            l.append(n//i)
    return l[::2] + l[-3 if l[-1]==l[-2] else -1::-2]

A, B = sorted(map(int, input().split()))
l = divisors(B-A)

solution = []
for d in l :
    n = d - A % d
    solution.append((n, lcm(A+n, B+n)))

if not solution :
    print(1)
else :
    print(min(solution, key=lambda x:x[1])[0])