import sys

N = int(sys.stdin.readline())


M, N = map(int, sys.stdin.readline().split())


#N
#1
#2
#3 
#...
#N
N = int(sys.stdin.readline())
for T in range(N) :
  X = int(sys.stdin.readline())



#N K
#1
#2
#3 
#...
#N
N, K = map(int, sys.stdin.readline().split())
for T in range(N) :
  X = int(sys.stdin.readline())



#N
#1 2
#2 3
#3 7
#N 5
N = int(sys.stdin.readline())
for T in range(N) :
  X, Y = map(int, sys.stdin.readline().split())



#N
#1 2 3 4 5 6 7 8 9 10
N = int(sys.stdin.readline())
l = map(int, sys.stdin.readline().split())




N = sys.stdin.readline()
M = sys.stdin.readline().rstrip().split()


#M N
#e1 e2 e3... eM
#eM+1 eM+2 ... e2M
#...
#eM-N+1... eMN
#큰 데이터를 다 저장할 때
import sys
N, M  = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]