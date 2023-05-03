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
  elif "pop" in command : #get
    if len(S) :
      i = 0 if command[4:9] == "front" else -1
      popped = S[i]
      del S[i]
      print(popped)
    else :
      print(-1)
  elif "push" in command : #put
    x = command.split()[1]
    if command[5:10] == "front" :
      S.insert(0, x)
    else :
      S.append(x)