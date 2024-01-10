import sys
input = sys.stdin.readline
write = sys.stdout.write

def toindex(c: chr) :
     return ord(c)-65

N = int(input())
tree = [False] * N
for T in range(N) :
    i, L, R = map(toindex, input().split())
    tree[i] = (L, R)

NONE = -19
def pre(i) :
    write(chr(i+65))
    if tree[i][0] != NONE :
        pre(tree[i][0])
    if tree[i][1] != NONE :
        pre(tree[i][1])

def mid(i) :
    if tree[i][0] != NONE :
        mid(tree[i][0])
    write(chr(i+65))
    if tree[i][1] != NONE :
        mid(tree[i][1])

def post(i) :
    if tree[i][0] != NONE :
        post(tree[i][0])
    if tree[i][1] != NONE :
        post(tree[i][1])
    write(chr(i+65))

pre(0)
write("\n")
mid(0)
write("\n")
post(0)