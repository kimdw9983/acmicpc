K = int(input())

l = []
for i in range(6) :
  l.append(input().rstrip())

W = H = Wi = Hi = 0
for i, v in enumerate(l) :
  dir = v[0]
  dis = int(v[2:]) #길이
  if dir == '4' or dir == '3' :
    if H < dis :
      Hi = i #가장 긴 너비의 index
      H = dis
  else :
    if W < dis :
      Wi = i
      W = dis

big = W * H
#가장 긴 (가로or세로)변의 양 옆에는 가장 긴 (가로<->세로)변이 반드시 존재한다.
smallH = abs(int(l[Wi-1][2:]) - int(l[Wi-5][2:])) 
smallW = abs(int(l[Hi-1][2:]) - int(l[Hi-5][2:]))
small = smallH * smallW
print(K * (big - small))