import itertools

alphabet = ["a","b","c"]

#nPr(순열) - 순서상관있고, 중복 없을 때
w = itertools.permutations(alphabet)
#abc, acb, bac, bca, cab, cba

#n^r(중복순열) - 순서 상관있고, 중복 포함할때
w = itertools.product(alphabet, repeat=2) #abc중에서 2개를 뽑는다
#aa, ab, ac, ba, bb, bc, ca, cb, cc

###순서 상관이 있는게 더 많음!!

#nCr(조합) - 순서 상관없고, 중복 없을때
w = itertools.combinations(alphabet, 2)
#ab, ac, bc
""" 부분 집합 모두 출력
for i in range(len(alphabet) + 1) :
    for c in itertools.combinations(alphabet, i) :
        print("".join(c))
"""

#nHr(중복조합) - 순서상관없고, 중복있을때
w = itertools.combinations_with_replacement(alphabet,3)
#aaa, aab, aac, abb, abc, acc, bbb, bbc, bcc, ccc

print(*list(map("".join, w)), sep=", ")