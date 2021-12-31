A,B,C=map(int,input().split())

l = [A%C]
b = 1 * l[0] if B&1 else 1
for i in range(1, B.bit_length()) :
    x = l[i-1]**2%C
    l.append(x)
    if B&(2**i) :
        b *= x

print(b%C)
########################################
print(pow(*map(int,input().split())))
#pow(a,b,c) : A^B%C를 효율적으로 처리.