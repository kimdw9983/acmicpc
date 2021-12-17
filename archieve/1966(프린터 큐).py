N = int(input())

for T in range(N) :
  length, M = map(int, input().split())
  l = [*enumerate(map(int, input().split()))]
  #print(l)

  cnt = 0
  while True :
    found = False
    for c in l[1:] : #높은게 있는지 탐색
      if l[0][1] < c[1] : #우선순위가 더 높은게 있는경우
        l.append(l.pop(0)) #뒤로 넘김
        found = True
        break
    
    if found :
      continue
    else : 
      pop = l.pop(0)
      if pop[0] == M :
        print(cnt+1)
        break
      else : 
        cnt += 1

"""
import collections

N = int(input())

for T in range(N) :
  length, M = map(int, input().split())

  d = collections.defaultdict(list)
  for i, v in enumerate(map(int,input().split())) :
    d[v].append(length-i-1)
  print(sorted(d.items(), reverse=True))
  
  answer = []
  for i in range(9) :
    answer += d[9-i]
  
  print(answer)

#틀린이유 : 출력에 필요한 알고리즘을 완전히 잘못 이해함.
#그래도 collections.defaultdict를 사용한 예시로 남겨둠
"""