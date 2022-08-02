import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def upward(S, a, tmp) :
	s = S[a]
	if s < 0: 
		return a, tmp
	tmp.append(a)
	return upward(S, s, tmp)

def find(S, a): #루트 찾기
	f, x = upward(S, a, [])
	for n in x :
		S[n] = f
	return f

def union(S, a, b):
	A = find(S, a) 
	B = find(S, b) 
	if A == B : return 

	if S[A] < S[B]: 
		S[B] = A
	elif S[A] > S[B]:
		S[A] = B
	else :
		S[A] -= 1
		S[B] = A

N, M = map(int,input().split())
S = [-1] * (N+1)
for _ in range(M):
	flag, a, b = map(int,input().split()) 
	if flag :
		sys.stdout.write(("YES" if find(S, a) == find(S, b) else "NO") + "\n")
	else :
		union(S, a, b)

###########################################################
#https://m.blog.naver.com/good5229/221819936100
#https://gmlwjd9405.github.io/2018/08/31/algorithm-union-find.html
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def union(S, a, b):
	A = find(S, a) #a정점의 root를 찾는다.
	B = find(S, b)
	if A == B :  
		#두 정점의 root가 같다는 의미
		#(= A와 B가 같은 집합에 속한다.)
		return

	#Union by rank(height) - O(1)
	"""연결리스트의 형태가 된다면 Union과 Find의 연산과정이 O(n)으로 될 수 있다(최악시간복잡도 case).
	따라서 두 트리를 합칠 때 높이가 높은 쪽을 root로 삼는다.
	"""
	if S[A] < S[B]:
		S[A] += S[B] #트리의 높이가 높은쪽으로 갱신해준다.
		S[B] = A     #B의 root가 A로 바뀌었음을 표시해준다.
	else:
		S[B] += S[A]
		S[A] = B

def find(S, x):
	if S[x] < 0: 
		"""문제에서 정의한 집합의 상태를 생각해보면
		1: {1}, 2: {2}, ... 등으로 자기 자신이 root라고 표현하고 있다.
		이것을 최적화 하여 문제의 집합S의 원소가 전부 -1으로 설정했다.
		-1은 자기 자신이 root라는 뜻 + 트리의 높이가 0이라는 뜻이다. """
		return x #원소 자기 자신이 root이면, 그대로 반환한다.
	S[x] = find(S, S[x]) #O(1)
	#(경로 압축) find하면서 만난 모든 값의 부모 노드를 root로 만든다.
	return S[x] 

##########################################