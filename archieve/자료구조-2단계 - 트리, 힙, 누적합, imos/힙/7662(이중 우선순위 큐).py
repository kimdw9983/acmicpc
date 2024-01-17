import sys, heapq
input = sys.stdin.readline
T = int(input())

def sync(q) :
    while q and not id[q[0][1]] :
        heapq.heappop(q)

for _ in range(T) :
    minh = []; maxh = []
    k = int(input())
    id = [False] * 1000001
    for i in range(k) :
        command = input().rstrip()

        if command[0] == "I" :
            n = int(command[2:])
            heapq.heappush(maxh, (-n, i))
            heapq.heappush(minh, (n, i))
            id[i] = True
        elif command[2] == "1" and maxh :# 최댓값
            sync(maxh)
            id[maxh[0][1]] = False
            heapq.heappop(maxh)
        elif command[2] == "-" and minh :
            sync(minh)
            id[minh[0][1]] = False
            heapq.heappop(minh)
        
        sync(maxh)
        sync(minh)
    
    if maxh :
        print(-maxh[0][0], minh[0][0])
    else :
        print("EMPTY")

#https://www.acmicpc.net/source/25921312
import sys, heapq
input = sys.stdin.readline
T = int(input())

for _ in range(T) :
    minh = []; maxh = []
    k = int(input())
    id = dict()
    for i in range(k) :
        command = input().rstrip()

        if command[0] == "I" :
            n = int(command[2:])
            if n in id :
                id[n] += 1
            else :
                id[n] = 1
                
            heapq.heappush(maxh, -n)
            heapq.heappush(minh, n)
            id[i] = True
        elif command[2] == "1" and maxh :# 최댓값
            id[maxh[0][1]] = False
            heapq.heappop(maxh)
        elif command[2] == "-" and minh :
            id[minh[0][1]] = False
            heapq.heappop(minh)
    
    if maxh :
        print(-maxh[0][0], minh[0][0])
    else :
        print("EMPTY")