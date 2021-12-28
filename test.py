import sys
N, r, c = map(int, sys.stdin.readline().split())

num = 0
while True :
    if r < 2 and c < 2 :
        num += r*2 + c
        break
    
    #p2r = int(math.log2(r)) #log2(x) x는 0보다 커야함.
    p2r = r.bit_length() - 1
    p2c = c.bit_length() - 1
    
    if not p2r - p2c : #p2r == p2c
        num += 4**p2r * 3
        r -= 2**p2r
        c -= 2**p2c
    elif p2r > p2c : 
        num += 4**p2r * 2 
        r -= 2**p2r
    else :
        num += 4**p2c
        c -= 2**p2c
    
print(num)