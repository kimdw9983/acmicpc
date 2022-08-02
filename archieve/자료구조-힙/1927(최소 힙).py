import heapq, sys
input = sys.stdin.readline
print = sys.stdout.write

heap = []
for i in range(int(input())) :
		X = input()

		if X == "0\n" or X == "0" :
				try :
						n = heapq.heappop(heap)
						print(str(n)+"\n")
				except :
						print("0\n")
		else :
				heapq.heappush(heap, int(X))