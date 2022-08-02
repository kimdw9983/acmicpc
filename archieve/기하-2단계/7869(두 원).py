import math
x1, y1, r1, x2, y2, r2 = map(float, input().split())

d = math.dist((x1, y1), (x2, y2))

if r1 + r2 <= d : #원이 곂치지 않음
	result = 0
elif abs(r1-r2) >= d : #내접
	result = min(r1, r2)**2 * math.pi
else :
	th1 = math.acos((r1**2 + d**2 - r2**2) / (2 * r1 * d)) * 2
	arc1 = (math.pi * r1**2 * math.degrees(th1) / 360) - (r1**2 * math.sin(th1) / 2)

	th2 = math.acos((r2**2 + d**2 - r1**2) / (2 * r2 * d)) * 2
	arc2 = (math.pi * r2**2 * math.degrees(th2) / 360) - (r2**2 * math.sin(th2) / 2)
	result = arc1 + arc2

print(format(round(result, 3), ".3f"))