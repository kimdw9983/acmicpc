x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def CCW(ax, ay, bx, by, cx, cy) :
	ccw = (bx-ax) * (cy-ay) - (cx-ax) * (by-ay)

	if ccw > 0 : return 1
	elif ccw < 0 : return -1
	return 0

#123*124 < 0 & 341*342 < 0
result = CCW(x1, y1, x2, y2, x3, y3) * CCW(x1, y1, x2, y2, x4, y4) < 0 and CCW(x3, y3, x4, y4, x1, y1) * CCW(x3, y3, x4, y4, x2, y2) < 0

print(1 if result else 0)