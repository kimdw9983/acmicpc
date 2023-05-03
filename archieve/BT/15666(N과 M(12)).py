import itertools, sys
n, k = map(int, input().split())
l = sorted(map(int, input().split()))
s = set()

for c in itertools.combinations_with_replacement(l, k) :
    s.add(c)

for c in sorted(list(s)) :
    for d in c :
        sys.stdout.write(str(d) + " ")
    sys.stdout.write("\n")