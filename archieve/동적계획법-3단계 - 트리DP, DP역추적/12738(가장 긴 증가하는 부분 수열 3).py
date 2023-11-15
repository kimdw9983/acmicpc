import sys, bisect
input = sys.stdin.readline
n = int(input())
DATA = tuple(map(int, input().split()))

bis = [-int(2e9)]#입력 가장 작은 값보다 낮아야 한다.
for num in DATA :
  if bis[-1] < num :
    bis.append(num)
  else :
    bis[bisect.bisect_left(bis, num)] = num

print(len(bis)-1)