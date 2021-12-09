T = [1,2,3,3,4,5]
#1개 필요할 때(가장 앞에 있는것만)
T.index(max(T))
#여러개 필요할 때
min(enumerate(T), key=lambda p: p[1])