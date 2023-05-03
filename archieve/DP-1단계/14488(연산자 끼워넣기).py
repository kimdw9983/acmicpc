input()
num = list(map(int, input().split()))
operators = list(map(int, input().split())) #+-x÷

solution = list()
def calc(sum, ops, op, level) :
  if op == 0 :
    sum += num[level]
  elif op == 1 :
    sum -= num[level]
  elif op == 2 :
    sum *= num[level]
  elif op == 3 :
    sum /= num[level]
    sum = int(sum)

  if level+1 >= len(num) :
    solution.append(sum)
    return

  for op, remaining in enumerate(ops) :
    if remaining :
      copied = ops[:]
      copied[op] -= 1
      calc(sum, copied, op, level+1)

calc(0, operators[:], 0, 0)
print(max(solution), min(solution), sep="\n")