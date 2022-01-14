import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
N = int(input().rstrip())
S = deque()
for T in range(N) :
		command = input().rstrip()

		if command == "front" :
				print(str(S[0])+"\n" if len(S) else "-1\n")
		elif command == "back" :
				print(str(S[-1])+"\n" if len(S) else "-1\n")
		elif command == "size" :
				print(str(len(S))+"\n")
		elif command == "empty" :
				print("0\n" if len(S) else "1\n")
		elif command == "pop" : #get
				if len(S) :
						print(str(S.popleft())+"\n")
				else :
						print("-1\n")
		else : #put
				x = command[5:]
				S.append(x)