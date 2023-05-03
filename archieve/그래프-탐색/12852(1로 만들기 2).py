import collections
X = int(input())
memo = {0:[]}

Q = collections.deque()
Q.append([X, 0])

while Q :
  v, last = Q.popleft()
  if v in memo :
    continue
  visited = memo[last] + [v]
  memo[v] = visited.copy()
  if v == 1 :
    break

  if not v % 3 :
    Q.append([v//3, v])
  if not v % 2 :
    Q.append([v//2, v])
  Q.append([v-1, v])

answer = memo[1]
print(len(answer) - 1)
print(" ".join(map(str, answer)))