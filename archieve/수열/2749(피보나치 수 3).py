N = int(input())
M = int(1e6)
a, b = 0, 1
for _ in range(N%(15*int(1e5))) :
	a, b = b%M, (a+b)%M

print(a)
#M이 10^k꼴이 아닐경우 다른 방법으로 해결해야한다.
#https://oeis.org/A001175 피사노 주기