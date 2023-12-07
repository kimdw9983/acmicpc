import sys, bisect
input = sys.stdin.readline
n = int(input())
DATA = tuple(map(int, input().split()))

bis = [0]
for num in DATA :
  if bis[-1] < num :
    bis.append(num)
  else :
    bis[bisect.bisect_left(bis, num)] = num

print(len(bis)-1)