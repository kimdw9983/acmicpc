@timeout(1)
def bin(n, k) : #메모리 최적화
  if(k > n // 2) : #이항계수의 성질(절반까지만 구하면 나머지는 대칭)
    k = n - k 
  B = [0] * (k+1)
  B[0] = 1
  for i in range(1, n+1) :
    j = min(i, k)
    while (j > 0) :
      B[j] = (B[j] + B[j-1])%1000000007
      j -= 1
  return B[k]

a, b = map(int, input().split())
print(bin(a, b))