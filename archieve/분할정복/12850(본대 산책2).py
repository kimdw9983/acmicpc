B = int(input())

N = 8
A = [
  [0,1,1,0,0,0,0,0],
  [1,0,1,1,0,0,0,0],
  [1,1,0,1,1,0,0,0],
  [0,1,1,0,1,1,0,0],
  [0,0,1,1,0,1,1,0],
  [0,0,0,1,1,0,0,1],
  [0,0,0,0,1,0,0,1],
  [0,0,0,0,0,1,1,0]
]

def calc(a, a_) :
  res = 0
  for i, v in enumerate(a) :
    res += v * a_[i]
  return res % 1000000007

def power(A) :
  A_ = list(zip(*A))
  AA = [[0] * N for i in range(N)]
  for i, l in enumerate(AA) : 
    for j, v in enumerate(l) :
      l[j] = calc(A[i], A_[j])
  return AA

dp = [A]
answer = [[0]*i+[1]+[0]*(N-i-1) for i in range(N)]
for b in range(B.bit_length()) :
  A = dp[-1]
  dp.append(power(A))
  if B&(1<<b) : #해당 비트가 1이면
    tmp = [[0] * N for _ in range(N)]
    for i, l in enumerate(tmp) :
      for j, v in enumerate(l) :
        l[j] = calc(answer[i], list(zip(*A))[j])
    answer = tmp

print(answer[0][0])