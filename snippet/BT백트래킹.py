#https://www.youtube.com/watch?v=Ar40zcPoKEI
KEYPAD = ["", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

input = "25"
result = list()


def BT(level, letter: str):  #Back Tracking
    #level : 깊이 / letter : sub-result, 결과list의 원소
    global input
    if level >= len(input):  #Recursion이 끝났을 때
        result.append(letter)
        return

    num = int(input[level])  #키패드의 무슨 버튼을 눌렀는지
    chars = KEYPAD[num]  #현재 레벨에서의 문자열들
    for c in chars:  #decision tree에서 갈라지는 부분
        BT(level + 1, letter + c)


BT(0, "")
print(result)


def permute(level, s):
    if level == 1:
        return s
    else:
        return [y + x for y in permute(1, s) for x in permute(level - 1, s)]

S = "Some String"
l = len(S)
def palindrome(i):
  if l - 2 * i <= 0 : return 1
  if S[i] == S[-i-1]: return palindrome(i+1)
  else: return 0