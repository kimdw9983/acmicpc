dict([(v, k) for k, v in DoGam.items()])
#key랑 value 스왑.
#(단 1:1 매칭하는 경우에만 사용 가능)
#이거 실행보다 입력받을 때 별도의 딕셔너리를 만드는게 나음(1620)

#list를 값 : 키 의 형태로 변환(1대1 매칭일때만 가능)
d = {v: k for k, v in enumerate(l))}
