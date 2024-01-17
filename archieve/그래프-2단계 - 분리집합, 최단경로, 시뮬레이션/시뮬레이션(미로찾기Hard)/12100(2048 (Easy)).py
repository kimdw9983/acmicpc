import sys
input = sys.stdin.readline

N = int(input())
l = []
for _ in range(N) :
  l.append([*map(int, input().split())])
#깊이가 깊어질때마다 맵 전체복사 해야함.

def move_h_(L, d) : #좌우
  new_L = []
  for i, _l in enumerate(L) : #맵 전체에 대해
    l = [*reversed(_l)] if d else _l #오른쪽명령이면 뒤집음
    for j in range(N) : #마지막 아이템이 아니면서,
      if l[j] :#값이 있을경우
        for k, v in enumerate(l[j+1:]) : #그 아이템의 오른쪽부터
          if v : #아이템 오른쪽에 다른 아이템이 있는데,
            if l[j] == v :#값도 같으면
              l[j] *= 2 #기존꺼 값 2배
              l[k+j+1] = 0 #그 아이템 제거
            break #합치기는 1번만 가능, 합치기에 실패할경우도 끝
    tmp = []
    zeros = 0
    for j, v in enumerate(l) :
      if v :
        tmp.append(v)
      else :
        zeros += 1
    new_L.append(([0] * zeros + tmp[::-1]) if d else (tmp + [0] * zeros))
  return new_L

def move_v(_L, d) : #상하
  L = []
  for _l in zip(*_L) : #배열 돌리기
    l = list(_l)
    tmp = []
    zeros = 0
    for j in range(N) :
      #객체속 값에 쓰기를 할 예정인경우 enumerate를 쓰면 안됨
      if l[j] :
        has = False#합친게 있었는지 확인하는 용도
        for k in range(j+1, N) :
          if l[k] :
            has = True
            if l[j] == l[k] :
              tmp.append(l[j]*2) #원래 값 2배
              l[k] = 0 #거기에 있었던 값 제거
            else :
              tmp.append(l[j], l[k]) #둘다 순서대로 추가
            break
        if not has : #합칠게 없었으면 그대로 넣는다.
          tmp.append(l[j])
      else : 
        zeros += 1

    tmp = [0] * zeros + tmp if d else tmp + [0] * zeros
    assert len(tmp) == len(l)
    L.append(tmp)

  new_L = []
  for _l in zip(*L) :
    new_L.append(list(_l))

  return new_L
##############################
def move_h(L, d) : #좌우
  global answer
  new_L = []
  for i, _l in enumerate(L) : #맵 전체에 대해
    l = [*reversed(_l)] if d else _l #오른쪽명령이면 뒤집음
    for j in range(N) : #마지막 아이템이 아니면서,
      if l[j] :#값이 있을경우
        for k, v in enumerate(l[j+1:]) : #그 아이템의 오른쪽부터
          if v : #아이템 오른쪽에 다른 아이템이 있는데,
            if l[j] == v :#값도 같으면
              l[j] *= 2 #기존꺼 값 2배
              l[k+j+1] = 0 #그 아이템 제거
            break #합치기는 1번만 가능, 합치기에 실패할경우도 끝
    tmp = []
    zeros = 0
    for j, v in enumerate(l) :
      if v :
        answer = max(answer, v)
        tmp.append(v)
      else :
        zeros += 1
    new_L.append(([0] * zeros + tmp[::-1]) if d else (tmp + [0] * zeros))
  return new_L

def move_v(_L, d) : #상하  
  global answer
  L = []
  for _l in zip(*_L) : #배열 돌리기
    l = list(_l)
    tmp = []
    zeros = 0
    for j in range(N) :
      #객체속 값에 쓰기를 할 예정인경우 enumerate를 쓰면 안됨
      if l[j] :
        has = False#합친게 있었는지 확인하는 용도
        for k in range(j+1, N) :
          if l[k] :
            has = True
            if l[j] == l[k] :
              x = l[j]*2 #원래 값 2배
              answer = max(answer, x)
              tmp.append(x) 
              l[k] = 0 #다음 값(이었던것)
            else :
              tmp.append(l[j]) #둘다 순서대로 추가
            break
        if not has : #합칠게 없었으면 그대로 넣는다.
          tmp.append(l[j])
      else : 
        zeros += 1

    tmp = [0] * zeros + tmp if d else tmp + [0] * zeros
    assert len(tmp) == len(l)
    L.append(tmp)

  new_L = []
  for _l in zip(*L) :
    new_L.append(list(_l))

  return new_L
  ########################################################33
  import sys
input = sys.stdin.readline

N = int(input())
l = []
answer = 0
for _ in range(N) :
  arr = [*map(int, input().split())]
  answer = max(answer, max(arr))
  l.append(arr)

def move(_L, d) : #좌우상하
  global answer
  L = []
  for _l in zip(*_L) if d&2 else _L : #배열 돌리기
    l = list(_l[::-1] if d&1 else _l)
    tmp = []
    zeros = 0 #0의 총갯수
    for j in range(N) :
      #객체속 원소에 쓰기를 할 예정인경우 enumerate를 쓰면 안됨
      if l[j] : #값이 있으면
        has = False#합친게 있었는지 확인하는 용도
        for k in range(j+1, N) :
          if l[k] :#다음 값을 찾은 경우
            if l[j] == l[k] : #다음값과 값이 같으면
              has = True
              x = l[j]*2 #원래 값 2배
              answer = max(answer, x)
              tmp.append(x) 
              l[k] = 0 #다음 값(이었던것)
            break
        if not has : #합칠게 없었으면 그대로 넣는다.
          tmp.append(l[j])
      else : 
        zeros += 1

    tmp = [0] * zeros + tmp[::-1] if d&1 else tmp + [0] * zeros
    assert len(tmp) == len(l)
    L.append(tmp)

  #answer = max(answer, max(map(max, L)))
  return list(zip(*L)) if d&2 else L #배열 돌리기(세로줄 <=> 가로줄)

def BT(level, l) :
  if level == 5 :
    return
  
  BT(level+1, move(l, 0))
  BT(level+1, move(l, 1))
  BT(level+1, move(l, 2))
  BT(level+1, move(l, 3))

BT(0, l)
print(answer)