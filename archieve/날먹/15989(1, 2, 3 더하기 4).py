dp = [1] + [0] * 10004
for i in range(1,4) :
    for j in range(i, 10001) :
        dp[j] += dp[j-i]

for T in range(int(input())) :
    print(dp[int(input())])
#정답수열 OEIS A001399
#https://www.acmicpc.net/source/36393367