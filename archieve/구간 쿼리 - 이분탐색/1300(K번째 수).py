N = int(input())
k = int(input())

def decision(X) :
  cnt = 0
  for i in range(1, N+1) :
    cnt += min(X//i, N) #min: 행의 갯수보다 크면 안된다.
  return cnt >= k

low = 1
high = k
while low <= high :
  mid = (low + high) // 2

  if decision(mid) :
    answer = mid
    high = mid - 1
  else :
    low = mid + 1
    
print(answer)