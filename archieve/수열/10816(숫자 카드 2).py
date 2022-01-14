import sys
input = sys.stdin.readline
input(); cards = map(int, input().split())
input(); occurs = map(int, input().split())

d = dict()
for i in cards :
	if i in d :
		d[i] += 1
	else :
		d[i] = 1

for i in occurs :
	if i in d :
		print(f"{d[i]}", end=" ")
	else :
		print("0", end=" ")	