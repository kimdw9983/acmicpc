import sys, math
input = sys.stdin.readline
N = int(input())
l = [0] * N
for i in range(N) :
    l[i] = int(input())

l.sort() #O(n log n)

def divisors(n : int) : #n의 모든 약수 출력 O(n^.5)
    #n == 0인경우는 입력에서 제외됐으므로 무시
    l = []
    for i in range(1, math.isqrt(n) + 1): 
        if not n % i:            
            l.append(i)
            l.append(n//i)
    return l[::2] + l[-3 if l[-1]==l[-2] else -1::-2]

x = divisors(l[-1]-l[0])[1:] #1은 모든 수의 약수이므로 제외

for i in l[1:-1] :
    tmp = []
    for j in x :
        if not (i-l[0])%j :
            tmp.append(j)
    x = tmp  

print(*x)