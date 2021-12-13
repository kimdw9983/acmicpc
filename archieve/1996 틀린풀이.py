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