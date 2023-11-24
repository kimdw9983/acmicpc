N, K, M = map(int, input().split())
"""
MAX = 2010
bin = [[1] + [0] * (MAX-1) for _ in range(MAX)]
for i, l in enumerate(bin) :
  for j, v in enumerate(l) :
    l[j] = (bin[i-1][j-1] + bin[i-1][j]) % M
"""
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

dMN = []
dMK = []
while True :
  if N == K == 0 :
    break
  dMN.append(N%M)
  dMK.append(K%M)
  N //= M
  K //= M
dMN = dMN[::-1]
dMK = dMK[::-1]

answer = 1
for i, v in enumerate(dMN) :
  if v < dMK[i] :
    answer = 0
    break
  else :
    answer *= bin(v, dMK[i])%M

print(answer%M)