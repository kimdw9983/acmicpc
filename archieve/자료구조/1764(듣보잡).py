import sys
r = sys.stdin.readline
M, N = map(int, r().split())

not_heard = set()
not_seen = set()
for _ in range(M) :
  not_heard.add(r().rstrip())

for _ in range(N) :
  not_seen.add(r().rstrip())

not_heard_neither_seen = sorted(list(not_heard & not_seen))
print(len(not_heard_neither_seen),*not_heard_neither_seen, sep="\n")