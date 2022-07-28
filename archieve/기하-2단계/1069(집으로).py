import math
X, Y, D, T = map(int, input().split())

AB = math.dist((0, 0), (X, Y))
cnt = AB // D #점프한 횟수
if T >= AB : #점프를 하는게 손해일 경우
	print(AB)
elif cnt == 0: #AB보다 점프거리가 더 긴경우
	print(min(AB, (T+D)-AB, 2*T))
else :
	left = abs(AB - cnt * D) #점프로 최대한 근접뒤 남은 거리
	#print(cnt*T + left, (cnt+1)*T, AB)
	print(min(cnt*T + left, (cnt+1)*T, AB))