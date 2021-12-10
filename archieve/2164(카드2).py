n = int(input())
print(n if (n&(~(n-1)))==n else (n^(1<<n.bit_length()-1))*2)