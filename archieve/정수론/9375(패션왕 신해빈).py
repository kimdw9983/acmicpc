#시간초과 풀이
import itertools, sys
input = sys.stdin.readline

for i in range(int(input())) :
		d = dict()
		T = int(input())
		for _ in range(T) :
				n, k = input().rstrip().split()
				d[n] = k
		
		

		cnt = 0
		for i in range(T) :
				for c in itertools.combinations(d.keys(), i+1) :
						l = []
						valid = True
						for v in c :
								if d[v] in l :
										valid = False
										break
								else :
										l.append(d[v])
								
						if valid :
								cnt += 1
		
		print(cnt)

###########################################3
import collections, sys
input = sys.stdin.readline

for i in range(int(input())) :
		l = list()
		T = int(input())
		for _ in range(T) :
				_, k = input().rstrip().split()
				l.append(k)
		
		res = 1
		for c in dict(collections.Counter(l)).values() :
				res *= (c+1)
		
		print(res-1)