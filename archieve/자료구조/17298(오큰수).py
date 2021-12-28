import sys
input = sys.stdin.readline
N = int(input())
A = [*map(int, input().split())]

l = [-1] * N #정답리스트
stack = [A[-1]]
for e, v in enumerate(A[-2::-1]) :
    i = N-e-2
    if v >= stack[-1] :
        while stack :
            if v < stack[-1] : 
                l[i] = stack[-1]
                break
            stack.pop()
        stack.append(v)
    else :
        l[i] = stack[-1]
        stack.append(v)

sys.stdout.write((" ".join(map(str, l))))