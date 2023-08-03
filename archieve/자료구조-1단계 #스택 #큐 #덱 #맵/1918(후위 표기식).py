form = input()
stack = []
answer = []
_priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

for c in form :
  if c == '(' :
    stack.append(c)
  elif c == ')' :
    while stack :
      p = stack.pop()
      if p == '(' :
        break
      answer.append(p)
  elif c in _priority :
    while stack and _priority[c] <= _priority[stack[-1]] :
      answer.append(stack.pop())
    stack.append(c)
  else :
    answer.append(c)

while stack :
  answer.append(stack.pop())

print(''.join(map(str, answer)))