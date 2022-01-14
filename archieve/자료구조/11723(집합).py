import sys
N = int(sys.stdin.readline().rstrip())

S = set()
for T in range(N) :
	command = sys.stdin.readline().rstrip()

	if command == "all" :
		S.update(range(1,21))
	elif command == "empty" :
		S = set()
	else : #hard-coded way
		c, x = command.split()
		x = int(x) #'1', '2'같은게 추가됨

		if c == "add" :
			S.add(x)
		elif c == "remove" :
			S.discard(x)
		elif c == "check" :
			sys.stdout.write('1\n' if x in S else '0\n')
		elif c == "toggle" :
			if x in S :
				S.discard(x)
			else :
				S.add(x)