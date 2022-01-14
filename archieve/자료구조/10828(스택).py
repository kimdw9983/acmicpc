import sys
N = int(sys.stdin.readline().rstrip())
S = []
for T in range(N) :
	command = sys.stdin.readline().rstrip()

	if command == "top" :
		print(S[-1] if len(S) else -1)
	elif command == "size" :
		print(len(S))
	elif command == "empty" :
		print(0 if len(S) else 1)
	elif command == "pop" :
		print(S.pop() if len(S) else -1)
	elif "push" in command :
		x = command.split()[1]
		S.append(x)