import sys
N = int(sys.stdin.readline())
l = list()
l.append([])
l.append(["1"])
l.append(["11", "2"])
l.append(["111", "21", "12", "3"])

for i in range(4,15) :
    s = set()
    for j in range(3, 0, -1) :
        for case in l[i-j] :
            for ci in range(len(case)+2) : 
                s.add(case[:ci]+ str(j) + case[ci:])
    l.append(list(s))

for T in range(N) :
  X = int(sys.stdin.readline())

#정답수열 : 트리보나치 수열(a(n) = a(n-1) + a(n-2) + a(n-3))
#OEIS A000073, A305442