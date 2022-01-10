import math
X, B = map(int, input().split())

dXB = []
if X == 0 :
	dXB.append('0')
elif B < 0 or X < 0 :
	while True :
		dXB.append((abs(B)-abs(X % B)) % abs(B)) #염병
		X = math.ceil(X / B)
		if X > 0 and X < abs(B) :
			dXB.append(X)
			break
		elif X == 0 :
			if B > 0 :
				dXB.append('-')
			break
else :
	while True :
		dXB.append(X%B)
		X //= B
		if X < B :
			dXB.append(X)
			break

print("".join(map(str, dXB[::-1])))