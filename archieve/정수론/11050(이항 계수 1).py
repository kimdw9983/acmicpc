def bin_recur(n, k):	#재귀적 풀이
		if (k == 0 or n == k):
				return 1
		else:
				return bin(n-1, k-1) + bin(n-1, k)


def bin_dynamic(n, k):
		B = [[0] * (k+1) for _ in range(n+1)]	#파스칼의 삼각형
		for i in range(n+1):
				for j in range(min(i, k)+1):	#3C2는 있어도 2C3은 존재하지 않음
						if (j == 0 or j == i):
								B[i][j] = 1
						else:
								B[i][j] = B[i-1][j-1] + B[i-1][j]
		return B[n][k]


def bin(n, k):	#메모리 최적화
		if (k > n // 2):	#이항계수의 성질
				k = n-k	#
		B = [0] * (k+1)
		B[0] = 1
		for i in range(1, n+1):
				j = min(i, k)
				while (j > 0):
						B[j] = B[j] + B[j-1]
						j -= 1
		return B[k]

N = int(input())
K = int(input())
print(bin(N, K))