###################################풀이 1 - log(N^3)?
import sys
N, M, B = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for T in range(N)]

answer = 9999999999
answer_i = -1
for x in range(257) : 
  num_to_break = 0
  num_to_place = 0
  for i in range(N) :
    for j in range(M) :
      block = grid[i][j]
      if x > block :
        num_to_place += (x - block)
      else :
        num_to_break += (block - x)

  if num_to_break + B < num_to_place :
    #해당 높이로 블럭을 둘 수 없는 경우. 
    #또한 그보다 높은 높이로도 평탄화할 수 없다.
    break
  else :
    if num_to_break * 2 + num_to_place <= answer : 
      answer = num_to_break*2 + num_to_place
      answer_i = x

print(answer, answer_i)
