T = [1,2,3,3,4,5]

#1개 필요할 때(가장 앞에 있는것만), index()는 탐색임에 주의
T.index(min(T))

#여러개 필요할 때
min(enumerate(T), key=lambda x: x[1])