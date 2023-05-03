input()
DP = list()
NONE = -9999
sum = NONE #분기점, 임시 합계

for s in input().split() :
  n = int(s)
  if n >= 0 :
    sum += (n-NONE) if sum == NONE else n  #양수면 더한다
  elif sum == NONE and n < 0 : 
    DP.append(n) #예제 3번 케이스 방지
  elif sum + n < 0 : #-999등의 케이스, 연속으로 더하는게 의미 없음
    if sum != NONE :
      DP.append(sum)
    sum = NONE
  else :
    DP.append(sum)
    sum += n
    DP.append(sum)
    
if sum != NONE : 
  DP.append(sum)

print(max(DP))