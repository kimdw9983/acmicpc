import re
P = "ab"
S = "abcbdfasdfbdfd"

#안곂치는 모든 패턴 갯수
print(len([*re.finditer(P, S)])) 

#곂치는 모든 패턴 갯수(IOIOI 시간초과 풀이)
left = 0
while True :
    match = re.search(P, S[left:])
    if not match :
        break
    #패턴 찾은 경우

    left += match.start() + 1