from collections import deque
N, K = map(int, input().split())
MAX = 100000
visited = [False] * (MAX+1)

def BFS() :
    level = 0
    Q = deque([N])
    while True : 
        nextQ = deque()
        while Q : 
            v = Q.popleft()
            visited[v] = True
            if v == K :
                return level

            for i in (v+1, v-1, v*2) :
                if i <= 100000 and i >= 0 and not visited[i] :
                    nextQ.append(i)

        Q = nextQ
        level += 1

print(DFS())
##########################################################
N, K = map(int, input().split())
MAX = 100000
visited = [False] * (MAX+1)

def BFS() :
    level = iter = 0
    sep = 1
    Q = [N]

    while Q : 
        v = Q[iter]
        visited[v] = True
        if v == K :
            return level
        iter += 1

        for i in (v+1, v-1, v*2) :
            if i <= 100000 and i >= 0 and not visited[i] :
                Q.append(i)
        
        if iter >= sep :
            sep = len(Q)
            level += 1        

print(DFS())