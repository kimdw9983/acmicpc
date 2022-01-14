import sys
input = sys.stdin.readline

T = int(input())
for i in range(T) :
		command = input().rstrip()
		l = input()[1:-2].split(',') if int(input()) else input()[1:-2]

		reversed = False
		error = False
		for c in command :
				if c == "R" :
						reversed = not reversed
				elif not l :
						error = True
						break
				else :
						l.pop(-1 if reversed else 0)
		
		out = sys.stdout.write
		if error :
				out("error\n")
		else :
				out("[" + ",".join(l[::-1 if reversed else 1]) + "]\n")