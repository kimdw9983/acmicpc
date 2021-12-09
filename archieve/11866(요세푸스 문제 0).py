N, K = map(int, input().split())
S = [i+1 for i in range(N)]

p = 0
answer = "<"
for i in range(N) :
  p = (p+(K-1)) % len(S)
  answer += str(S.pop(p)) + ", "

print(answer[:-2] + ">")