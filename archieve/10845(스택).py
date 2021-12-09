import sys
N = int(sys.stdin.readline().rstrip())
S = []
for T in range(N) :
  command = sys.stdin.readline().rstrip()

  if command == "front" :
    print(S[0] if len(S) else -1)
  elif command == "back" :
    print(S[-1] if len(S) else -1)
  elif command == "size" :
    print(len(S))
  elif command == "empty" :
    print(0 if len(S) else 1)
  elif command == "pop" : #get
    if len(S) :
      popped = S[0]
      del S[0]
      print(popped)
    else :
      print(-1)
  elif "push" in command : #put
    x = command.split()[1]
    S.append(x)