import sys
input = sys.stdin.readline
S = input().rstrip()
acc = []
for alphabet in range(26) :
	l = []
	sum = 0
	c = chr(97 + alphabet)
	for i, v in enumerate(S) :
		sum = sum+1 if c == v else sum
		l.append(sum)
	acc.append(l)

q = int(input())
res = []
for _ in range(q) :
	x, l, r = input().split()
	l = int(l);r = int(r)

	s = acc[ord(x)-97]
	res.append((0 if (l != 0 and s[l-1] == s[l]) or (l == 0 and s[0] == 0) else 1) + s[r] - s[l])

print("\n".join(map(str, res)))