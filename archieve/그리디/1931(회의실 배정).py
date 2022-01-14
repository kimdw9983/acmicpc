import sys
N = int(sys.stdin.readline())

l = list()
for T in range(N) :
		X, Y =	map(int, sys.stdin.readline().split())
		l.append((X,Y))

l.sort(key= lambda x: (x[1], x[0]))

end = cnt = 0
for t in l :
		if t[0] >= end :
				cnt += 1
				end = t[1]
				
print(cnt)
#난 바보야..
"""
for t in l :
		if not (d - c) or t[0] >= end : #이번 시작시간t[0]이 이전 끝나는 시간 [이상], 즉 곂치지 않는 시간일 경우
				start = t[0]
				end = t[1]
				possible.append(t)
		elif t[0] == end and (end - start) > (t[1] - t[0]) : #회의 소요기간이 더 짧을때
				possible[-1] = t
				start = t[0]
				end = t[1]
"""
"""
start, end = 0, 0
cnt = 0
for t in l :
		#print(t, start, end)
		if end <= t[0] :
				start = t[0]
				end = t[1]
				cnt += 1
		elif end > t[0] and ((t[1] - t[0]) < (end - start) or t[0] == t[1]) :
				start = t[0]
				end = t[1]

print(cnt)
"""