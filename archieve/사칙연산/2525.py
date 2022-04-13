import sys

input = sys.stdin.readline
A, B = map(int, input().split())
C = int(input())

print((A + C//60 + (1 if B+C%60 >= 60 else 0))%24, (B + C%60)%60)