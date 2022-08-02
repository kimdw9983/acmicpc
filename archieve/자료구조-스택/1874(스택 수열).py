import sys
N = int(input())

def poop(S) :
	try :
		poop = S.pop()
	except :
		return -1
	return poop

counter = 1
S = [] #stack
answer = []
for _ in range(N) :
	i = int(sys.stdin.readline())
	if counter <= i : #증가하는경우 i까지 증가시키고 pop
		for _ in range(i - counter + 1) :
			answer.append('+')
			S.append(counter)
			counter += 1
		S.pop()
		answer.append('-')
	else :
		popped = poop(S)
		if popped != i :
			print("NO",end="")
			answer = []
			break
		answer.append('-')
	

print(*answer, sep="\n")