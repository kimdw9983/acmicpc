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
pow(1,2,3)


#분할 정복을 이용한 거듭제곱
dp = [0000] #초기값 넣기
B = 1234
for b in range(B.bit_length()) : #b = bit
  x = dp[-1]
  dp.append(x * x) #제곱한걸 넣는다
  if B&(1<<b) : 
    pass
B % 1234567891 #대충 마무리 작업


#자릿수
import math
math.log10