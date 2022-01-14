import sys
input = sys.stdin.readline

N = int(input())
D = [*map(int, input().split())] #distance
P = [*map(int, input().split())] #price

last = P[0]
#더 싼걸 찾을 때까지 거리당 가격으로 삼
dist = D[0]
sum = 0
for i in range(1, len(D)) :
		if last <= P[i] : 
				dist += D[i]
		else :
				sum += last*dist
				last = P[i]
				dist = D[i]

print(sum + dist * last)