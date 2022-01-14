import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = [*map(int, input().split())]
l = [*range(1, N+1)]

p = 0
answer = 0
while S :
		x = S.pop(0)
		offset = 0
		while True :
				if l[(p+offset) % len(l)] == x :
						p = (p+offset) % len(l)
						l.pop(p)
						break
				elif l[(p-offset) % len(l)] == x :
						p = (p-offset) % len(l)
						l.pop(p)
						break
				offset += 1
		answer += offset

print(answer)