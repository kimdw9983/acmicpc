import sys
N, M = map(int, sys.stdin.readline().split())
DoGam = [0] * (N + 1)
UnDoGam = dict()
answers = []
for i in range(N) :
  X = sys.stdin.readline().rstrip()
  DoGam[i+1] = X
  UnDoGam[X] = i+1

#UnDoGam = dict([(v, k) for k, v in DoGam.items()])
#입력받을 때 바꾸는게 낫다
for _ in range(M) :
  x = sys.stdin.readline().rstrip()
  answers.append(DoGam[int(x)] if x.isdigit() else str(UnDoGam[x]))

print(*answers, sep="\n")
print("\n".join(answers)) #이게 가장 빨랐음