import sys, collections
input = sys.stdin.readline
N = int(input())
M = int(input())

graph = collections.defaultdict(set)
def connect(n1, n2) :
	graph[n1].add(n2)
	graph[n2].add(n1) #유향(directed)그래프 일경우 해당 없음.

for _ in range(M) :
	n1, n2 = input().split()
	connect(n1, n2)

visit = list()
queue = list()
answer = set()

queue.append('1')

while queue :
	node = queue.pop(0)
	if node not in visit :
		visit.append(node)
		answer.add(node)
		queue.extend(graph[node])

print(len(answer)-1) #자기 자신노드 제외(-1)