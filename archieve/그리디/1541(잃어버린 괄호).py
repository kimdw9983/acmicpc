F = input()

operand = "0"
is_sub = False #첫번째 -가 나온 이후부터는 무조건 빼기만 할 것이므로
sum = 0
for c in F :
		if c == "+" :
				sum += int(operand) * (-1 if is_sub else 1)
				operand = "0"
		elif c == "-" :
				sum += int(operand) * (-1 if is_sub else 1)
				operand = "0"
				is_sub = True
		else :
				operand += c
sum += int(operand) * (-1 if is_sub else 1)

print(sum)