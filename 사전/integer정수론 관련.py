def gcd(m,n):
  while n != 0:
    t = m%n
    (m,n) = (n,t)
  return abs(m)
#최소공배수 = ab/gcd(a,b)