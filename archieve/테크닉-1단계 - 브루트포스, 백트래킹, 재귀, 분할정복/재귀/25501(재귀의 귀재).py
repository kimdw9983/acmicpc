def ri(s, l, r, cnt):
  cnt += 1
  if l >= r: return (1, cnt)
  elif s[l] != s[r]: return (0, cnt)
  else: return ri(s, l+1, r-1, cnt)

for _ in range(int(input())) :
  s = input()
  print(*ri(s, 0, len(s)-1, 0))