def union(S, a, b):
	A = find(S, a)
	B = find(S, b)
	if A == B : return 

	#union-by-height
	if S[A] < S[B]:
		S[A] += S[B] #트리의 높이가 높은쪽으로 갱신해준다.
		S[B] = A     #B의 root가 A로 바뀌었음을 표시해준다.
	else:
		S[B] += S[A]
		S[A] = B

def find(S, x):
	if S[x] < 0: #자기 자신이 root이면
		return x
	S[x] = find(S, S[x])
	return S[x]

def union(S, C, a, b): 
	A = find(S, a)
	B = find(S, b)
	if A == B : return
		
	#노드 갯수 구하기
	S[B] = A
	C[A] += C[B]
	C[B] = 1