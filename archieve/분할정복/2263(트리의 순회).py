import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
mid = input().rsplit()
pos = {v: k for k, v in enumerate(mid)} #O(1) 만에 찾기 위함
post = input().rsplit()

answer = []

def DIV(a,b, c,d) : #(mid), (post)
  if (a > b) or (c > d) :
    return

  p = post[d]
  answer.append(p) 

  left = pos[p] - a
  right = b - pos[p]

  #DIV(mid[l-i:], post[l-i-1:-1]) 메모리 초과할듯
  #DIV(mid[:l-i-1], post[:l-i-1])
  DIV(a, a+left-1, c, c+left-1)
  DIV(b-right+1, b, d-right, d-1)

DIV(0, N-1, 0, N-1)
sys.stdout.write(' '.join(map(str, answer)))

#iterative solution: https://www.acmicpc.net/source/37158492