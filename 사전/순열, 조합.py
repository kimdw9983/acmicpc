import itertools

#nPr(순열) - 순서상관있고, 중복 없을 때
alphabet = ["a","b","c"]
w = itertools.permutations(alphabet)
#abc, acb, bac, bca, cab, cba

#n^r(중복순열) - 순서 상관있고, 중복 포함할때
w = itertools.product(alphabet, repeat=2) #abc중에서 2개를 뽑는다
#aa, ab, ac, ba, bb, bc, ca, cb, cc

#nCr(조합) - 순서 상관없고, 중복 없을때
w = itertools.combinations(alphabet, 2)
#ab, ac, bc

#nHr(중복조합) - 순서상관없고, 중복있을때
w = itertools.combinations_with_replacement(alphabet,3)
#aa, ab, ac, bb, bc, cc

print(*list(map("".join, w)), sep=", ")