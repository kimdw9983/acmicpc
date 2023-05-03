import sys, re
input = sys.stdin.readline

result = []
while True :
  s = input().strip()
  l = s.split() #split에 스페이스바 떼기 의존
  valid = False
  for c in l :
    if c != "$" :
      valid = True
  if not valid : break
    
  stack = list()

  for c in s :
    if c.islower() or c == "(" or c.isnumeric() :
      stack.append(c)
    elif c == ")" :
      b = []
      num = ""
      while True :
        c = stack.pop()
        if c == "(" : break
        if c.isnumeric():
          num += c
        else:
          b.append(c)
      stack.append("".join(map(str, b[::-1])) * int(num[::-1]) if num else 1)

  if stack :
    result.append("".join(map(str, stack)))

if result :
  print("\n".join(map(str, result)))