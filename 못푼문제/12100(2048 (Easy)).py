import sys
input = sys.stdin.readline

N = int(input())
l = []
answer = 0
for _ in range(N) :
	arr = [*map(int, input().split())]
	answer = max(answer, max(arr))
	l.append(arr)

def move(_L, d) : #좌우상하
	global answer

	L = []
	for _l in zip(*_L) if d&2 else _L : #배열 돌리기
		l = list(_l)
		tmp = []
		zeros = 0 #0의 총갯수
		for j in range(N) :
			#객체속 원소에 쓰기를 할 예정인경우 enumerate를 쓰면 안됨
			if l[j] : #값이 있으면
				has = False#합친게 있었는지 확인하는 용도
				for k in range(j+1, N) :
					if l[k] :#다음 값을 찾은 경우
						if l[j] == l[k] : #다음값과 값이 같으면
							has = True
							x = l[j]*2 #원래 값 2배
							answer = max(answer, x)
							tmp.append(x) 
							l[k] = 0 #다음 값(이었던것)
						break
				if not has : #합칠게 없었으면 그대로 넣는다.
					tmp.append(l[j])
			else : 
				zeros += 1

		tmp = [0] * zeros + tmp if d&1 else tmp + [0] * zeros
		assert len(tmp) == len(l)
		L.append(tmp)
	#pprint(list(zip(*L)) if d&2 else L)

	return list(zip(*L)) if d&2 else L #배열 돌리기(세로줄 <=> 가로줄)

def BT(level, l) :
	if level == 5 :
		return

	BT(level+1, move(l, 0))
	BT(level+1, move(l, 1))
	BT(level+1, move(l, 2))
	BT(level+1, move(l, 3))

BT(0, l)
print(answer)