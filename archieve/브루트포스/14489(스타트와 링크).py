import itertools

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
case = []

for team in list(itertools.combinations(members, N//2)):
	case.append(team)

def get_power(team) :
	power = 0 
	for i in range(N//2) :
		member = team[i] 
		for j in team:
			power += S[member][j] 

	return power

power_gaps = list()
for i in range(len(case)//2):
	power_gaps.append(abs(get_power(case[i]) - get_power(case[-i-1])))
		
print(min(power_gaps))