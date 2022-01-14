import sys

sudoku = list()
for i in range(9) :
	sudoku.append(list(map(int, input().split())))

def get_elements_in_div(a,b) :
	div = a//3 *3 + b//3
	return [sudoku[i//3+(div//3)*3][i%3+(div%3)*3] for i in range(9)]

def validate(a, b, x) :
	global sudoku

	if x in sudoku[a] :
		return False
	elif x in [sudoku[i][b] for i in range(9)] :
		return False
	elif x in get_elements_in_div(a,b) :
		return False
	return True

def get_next_node(a,b) :
	idx = a*9 + b
	for i in range(idx, 9*9) :
		if not sudoku[i//9][i%9] :
			return i//9, i%9
	return 9999, 9999

def solve(pos) :
	global sudoku
	a, b = pos
	if a > 8 : #탈출
		for l in sudoku :
			print(*l)
		sys.exit(0)
		return
	
	for case in range(1, 10) :
		if validate(a, b, case) :
			sudoku[a][b] = case
			solve(get_next_node(a, b))
			sudoku[a][b] = 0

solve(get_next_node(0,0))
print(*sudoku, sep="\n")