import math

M = int(input())
def C(n, k) : #nCk
	sum = 1
	for i in range(k) :
		sum *= (n-i)
	return sum//math.factorial(k)

def approx(m, n) : #C(n, k)의 유사값을 구하기 위한 역함수이다.
	#C(n, k) = (n-k)(n-k+1)(n-k+2)...n / k! = M(문제의 입력)
	#위 식에서 (n-k)(n-k+1)...n의 가운데에 있는 (n-k/2)를 m이라고 두면
	#m^n ≒ M인 성질을 이용해 근삿값(어짜피 부동소숫점이라 부정확)을 구한다. 
	#주워진 M의 크기가 커질수록 오차범위가 늘어나기 때문에 
	#적당히 그 주변의 값을 무작위 대입해서 C(m, k) == M이 될때까지 반복해서 해를 구함
	return (math.factorial(n)*m)**(1/n) + (n-1)/2

answers = list()
Threshold = 0.1 #값이 충분히 커지면 Threshold도 사용해야할 수 있다.
MAX_ITERATE = 2 #2~10^15 범위 내에선 +-2정도의 오차범위 내에서 해결할 수 있다.
for k in range(2, 30) :
	n = round(approx(M, k))
	TRH = min(int(n*Threshold),MAX_ITERATE)
	for a in range(1+2*TRH) :
		if C(n-TRH + a, k) == M : 
			answers.append([n-TRH+a, k])
			break
answers.append([M, 1])

for v in answers :
	if [v[0], v[0]-v[1]] not in answers :
		answers.append([v[0], v[0]-v[1]])

answers.sort(key = lambda x:(x[0], x[1]))
print(len(answers))
for [a, b] in answers :
	print(f"{a} {b}")