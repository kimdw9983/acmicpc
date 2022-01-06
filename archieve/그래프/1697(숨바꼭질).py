from collections import deque
N, K = map(int, input().split())
MAX = 100000
W = [0] * (MAX+1)
Q = deque([N])

while Q : 
    v = Q.popleft()
    if v == K :
        print(W[v])
        break

    for nv in (v+1, v-1, v*2) :
        if 0 <= nv <= MAX and not W[nv] :
            W[nv] = W[v] + 1
            Q.append(nv)
###########################################################
#visited를 True와 False만 기록한 코딩
#(예상과 달리 메모리도, 시간도 더 걸림)
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

print(BFS())
##########################################################
#덱을 사용하지 않으면서 visited에 True/False만 기록한 코딩
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

print(BFS())
#######################################################
#매우 깔끔하고 빠른 풀이
def find(n, k):
    if n >= k:
        return n-k
    elif k == 1:
        return 1
    elif k%2:
        return min(find(n, k-1), find(n, k+1)) + 1
    else:
        return min(k-n, find(n, k//2) + 1)
  
import sys
n, k = map(int, sys.stdin.readline().split())
print(find(n, k))