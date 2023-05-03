N = int(input())
DIGITS = 10

dp = [[0 for _ in range(1 << DIGITS)] for _ in range(DIGITS)] #dp[자릿수][비트마스크]
for d in range(1, DIGITS) :
  dp[d][1 << d] = 1

for level in range(N-1) :
  next_dp = [[0 for _ in range(1 << DIGITS)] for _ in range(DIGITS)]

  for d in range(DIGITS) : #digit
    for bit in range(1<<DIGITS): #bit, num
      next_dp[d][bit | (1 << d)] = next_dp[d][bit | (1 << d)] + (dp[d-1][bit] if d != 0 else 0) + (dp[d+1][bit] if d != 9 else 0)

  dp = next_dp

result = 0
for i in range(10) :
  result += dp[i][(1<<10)-1]

print([0,0,0,0,0,0,0,0,0,1,3,14,37,117,287,770,1800,4420,9994,23249,51307,115156,249487,546042,1166004,2505150,5287425,11200451,23414399,49050151,101720223,211185500,434991097,896444595,835729973,759735100,660371284,606485403,657835457,203722859,732382676,62947013,711953864,282534432,532704326,533430656,490303185,719078464,867439170,928508497,826187014,717575892,566595461,320670363,655531616,186881287,277343131,272775098,352307918,913419265,227796381,837613318,359667139,624615740,709094500,932384013,157643024,646028283,396360486,169463574,365015614,942074982,423530743,451163035,615483377,21727607,324705955,306613175,326811178,606166739,701478626,613754961,205272431,472587513,735855947,910895829,510318720,529015082,557887447,384840782,896423761,280533566,960515389,301710744,609183295,940630118,923402943,431914107,270442392,670667793][int(input())-1])