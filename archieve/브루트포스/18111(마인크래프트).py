###################################풀이 1 - log(N^3)?
import sys
N, M, B = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for T in range(N)]

answer = 9999999999
answer_i = -1
for x in range(257) : 
	num_to_break = 0
	num_to_place = 0
	for i in range(N) :
		for j in range(M) :
			block = grid[i][j]
			if x > block :
				num_to_place += (x - block)
			else :
				num_to_break += (block - x)

	if num_to_break + B < num_to_place :
		#해당 높이로 블럭을 둘 수 없는 경우. 
		#또한 그보다 높은 높이로도 평탄화할 수 없다.
		break
	else :
		if num_to_break * 2 + num_to_place <= answer : 
			answer = num_to_break*2 + num_to_place
			answer_i = x

print(answer, answer_i)
######################################풀이2 log(N^2)
import sys
from collections import Counter

input = sys.stdin.readline

def minecraft(g, b):
	gg = Counter(g)
	ret = []
	for h in range(max(gg.keys()), -1, -1):
		gt = 0
		inventory = b
		needed = 0
		for gh, gc in gg.items():
			# 지정 높이(h)보다 높은 곳은 깍아서 인벤토리로
			if h < gh:
				inventory += (gh - h) * gc
				gt += 2 * (gh - h) * gc
			# 지정 높이(h)보다 낮은 곳은 갯수 확인
			elif h > gh:
				needed += (h - gh) * gc
				gt += (h - gh) * gc

		# 지정된 높이(h)보다 작은 곳을 채울 블록이 있는지 확인
		if inventory >= needed:
			ret.append([gt, h])
		# 없으면 한칸 내려감
		
	ret.sort(key=lambda x: (x[0], -x[1]))
	#x[0]은 증가하는 순서, x[1]은 감소하는 순서로 정렬
	return ret[0] #x[0]이 가장 작고, x[1]가 가장 큼

N, M, B = map(int, input().split())
grounds = []
for _ in range(N):
	grounds.extend(list(map(int, input().split())))
res = minecraft(grounds, B)
print(res[0], res[1])