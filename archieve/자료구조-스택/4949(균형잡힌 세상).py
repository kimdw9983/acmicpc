import re, sys

while True :
	line = sys.stdin.readline().rstrip()
	if line == "." :
		break

	sep = []
	valid = True
	for m in re.finditer('[\(\)\[\]]', line) :
		c = m.group()
		if c == "(" or c == "[" :
			sep.append(c)
		elif sep and ((c == ")" and sep[-1] == "(") or (c == "]" and sep[-1] == "[")) :
			sep.pop()
		else :
			valid = False
			break
	valid = valid and not len(sep)
	
	print("yes" if valid else "no")