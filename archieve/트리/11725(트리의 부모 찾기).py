import sys, collections
input = sys.stdin.readline
N = int(input())
graph = [[] for i in range(N+1)]
parent = [0] * (N+1)

def connect(n1, n2):
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(N-1) :
    connect(*map(int, input().split()))

def DFS(start):
    s = [start]
    while s:
        v = s.pop()
        for i in graph[v]:
            if parent[i] == 0:
                parent[i] = v
                s += [i]        

def BFS(start):
    s = collections.deque([start])
    while s:
        v = s.popleft()
        for i in graph[v]:
            if parent[i] == 0:
                parent[i] = v
                s += [i]        


BFS(1)
for c in parent[2:] :
    sys.stdout.write(str(c) + "\n")