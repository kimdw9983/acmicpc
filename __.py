def sol() :
  N, M = map(int, input().split()) #가로 세로
  G = [[*input()] for _ in range(N)]
  DP = [[0] * (1 << (M+1)) for _ in range(N * M + 1)]  #i칸까지 채우고 지금까지 채운 최근 M+1칸의 상태(밀고난 다음에 추가)
  for i in range(N * M) :
    for j in range(1 << (M+1)) :
      possible = False

      if G[i//M][i%M] != 'x' : #배치할 자리가 이미 부숴진 자리면 안된다
        if i < M  : #M이하라면 왼쪽만 확인하면 된다.
          possible = j & (1 << M) == 0
        else:
          if i % M == 0 : #왼쪽 끝에 있는 경우: 우상
            possible = j & (1 << 2) == 0
          elif i % M == M-1 : #오른쪽 끝에있는 경우: 좌, 좌상
            possible = j & (1 << M | 1 << 0) == 0
          else : #그 외의 경우 : 좌, 우상, 좌상
            possible = j & (1 << M | 1 << 2 | 1 << 0) == 0

      if possible :
        DP[i+1][j >> 1 | 1 << M] = max(DP[i+1][j >> 1 | 1 << M], DP[i][j] + 1)
      else :
        DP[i+1][j >> 1] = max(DP[i+1][j >> 1], DP[i][j])

  print(max(DP[-1]))  
  debug(bin(DP[-1].index(max(DP[-1]))))
  debug(bin(1 << M))

for _ in range(int(input())):
  sol()

;; 17
;; 2 3
;; ...
;; ...
;; 2 3
;; x.x
;; xxx
;; 2 3
;; x.x
;; x.x
;; 10 10
;; ....x.....
;; ..........
;; ..........
;; ..x.......
;; ..........
;; x...x.x...
;; .........x
;; ...x......
;; ........x.
;; .x...x....
;; 10 10
;; xxxxxxxxxx
;; xxxxxxxxxx
;; xxxxxxxxxx
;; xxxxxxxxxx
;; xxxxxxxxxx
;; xxxxxxxxxx
;; xxxxxxxxxx
;; xxxxxxxxxx
;; xxxxxxxxxx
;; xxxxxxxxxx
;; 3 3
;; xx.
;; xxx
;; x.x
;; ;;6
;; 3 5
;; ..x..
;; ..x..
;; .xxx.
;; 1 6
;; ..x...
;; 10 10
;; .x.x...x..
;; .x..x.....
;; x.x.......
;; .x.x......
;; x...x.....
;; .x.x...x..
;; .x..x.....
;; x.x.......
;; .x.x......
;; x...x.....
;; 5 10
;; .x.x...x..
;; .x..x.....
;; x.x.......
;; .x.x......
;; x...x.....
;; 5 8
;; .x...x..
;; ..x.....
;; x.......
;; .x......
;; ..x.....
;; 5 7
;; x...x..
;; .x.....
;; .......
;; x......
;; .x.....
;; 4 3
;; x.x
;; x..
;; .x.
;; .xx
;; 3 4
;; .x.x
;; .xx.
;; x.x.
;; 5 4
;; x.x.
;; .x.x
;; x.x.
;; x..x
;; ..xx
;; 10 10
;; .x.x...x..
;; .x..x.....
;; x.xx..x...
;; .x.x....x.
;; x...x.x...
;; .x.x...x..
;; .x..x...x.
;; x.x.......
;; .x.x......
;; x.........
;; 10 10
;; xxxxxxxxxx
;; ..........
;; ..........
;; xxxxxxxxxx
;; ..........
;; xxxxxxxxxx
;; .........x
;; ...x......
;; ........x.
;; xxxxxxxxxx
1
3 5
..x..
..x..
.xxx.