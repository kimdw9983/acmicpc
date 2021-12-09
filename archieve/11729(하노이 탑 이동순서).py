import sys

def hanoi(level,start,goal):
    memo = {}
    def innerHanoi(level,start,goal):
        if (level,start,goal) in memo:
            return memo[(level,start,goal)]
        else:
            if level==1:
                returnStr = str(start) + " " + str(goal)
            else:
                goalTemp = next(x for x in [1,2,3] if (x!=start and x!=goal))
                returnStr = "\n".join(char for char in [innerHanoi(level-1,start,goalTemp),
                    str(start) + " " + str(goal),
                    innerHanoi(level-1,goalTemp,goal)])
            memo[(level,start,goal)] = returnStr
            return returnStr
    print(innerHanoi(level,start,goal))
        
N = int(sys.stdin.readline())
print(2**N-1)
hanoi(N,1,3)