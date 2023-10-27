A,B,C=map(int,input().split())

dp = [A%C]
X = 1
for b in range(B.bit_length()) :
  x = dp[-1]
  dp.append(x**2 % C)
  if B&(1<<b) :
    X *= x
    
print(X%C)
########################################
print(pow(*map(int,input().split())))
#pow(a,b,c) : A^B%C를 효율적으로 처리.