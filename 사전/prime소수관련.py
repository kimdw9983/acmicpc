import math
def is_prime(n):
    #https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = math.isqrt(n)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


def eratosthenes(n):
    #https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
    prime = [False] * 2 + [True for i in range(n - 1)]

    p = 2
    while (p * p <= n):
        if prime[p]:
            for i in range(p**2, n + 1, p):
                prime[i] = False
        p += 1

    for i, v in enumerate(prime):
        if v:
            print(i)
