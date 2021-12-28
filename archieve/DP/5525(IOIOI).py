import sys
input = sys.stdin.readline
P = int(input())
input()
S = input()

l = list()
for i, v in enumerate(S) :
    if v == "I" :
        l.append(i)

cnt = 0 #index가 2씩 증가하는 패턴이 연속으로 몇번 나왔는지
answer = 0
for i in range(1, len(l)) :
    if l[i] - l[i-1] == 2 :
        cnt += 1
    else :
        cnt = 0
    
    if cnt >= P :
        answer += 1

print(answer)