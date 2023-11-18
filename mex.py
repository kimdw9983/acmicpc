import io, os, sys, operator
input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

class LST:
  def __init__(self, L, f, fl, fll, node=0, lnode=0):
    self.f = f
    self.fl = fl
    self.fll = fll
    self.node = node
    self.lnode = lnode
    self.len = len(L)
    self.seg = [node] * self.len + L
    self.lazy = [lnode] * self.len
    self.cnt = [0] * self.len + [1] * self.len

    for i in reversed(range(self.len)):
      self.seg[i] = self.f(self.seg[i*2], self.seg[i*2+1])
      self.cnt[i] = self.cnt[i*2] + self.cnt[i*2+1]

  def _push(self, i, x) :
    self.seg[i] = self.fl(self.seg[i], x, self.cnt[i])
    if i < self.len :
      self.lazy[i] = self.fll(self.lazy[i], x)

  def _apply(self, i) :
    if self.lazy[i] == self.lnode: return
    self._push(i*2, self.lazy[i])
    self._push(i*2+1, self.lazy[i])
    self.lazy[i] = self.lnode 

  def _propagate(self, i):
    for h in reversed(range(1, self.len.bit_length()+1)) :
      if idx := i >> h : self._apply(idx)

  def _build(self, i) :
    while i :
      if i < self.len :
        self._apply(i)
        self.seg[i] = self.f(self.seg[i*2], self.seg[i*2+1])
      i >>= 1

  def mex(self) :
    res = 1
    i = 1
    while i < self.len :
      self._apply(i)
      if self.seg[i*2] != self.cnt[i*2] :
        assert self.seg[i*2] < self.cnt[i*2]
        i = i*2
      else :
        res += self.cnt[i*2]
        i = i*2+1
    return res

  def update(self, s, e, x):
    s += self.len
    e += self.len
    self._propagate(s)
    self._propagate(e-1)
    _s = s
    _e = e

    while s < e :
      if s & 1 :
        self._push(s, x)
        s += 1
      if e & 1 :
        e -= 1
        self._push(e, x)
      s >>= 1
      e >>= 1
    
    self._build(_s)
    self._build(_e - 1)
  
MAX = 10 ** 18 + 1
def sol() :
  N = int(input())
  Q = []
  for _ in range(N) :
    Q.append(list(map(int, input().split())))
  
  f = operator.add
  fl = lambda i, x, cnt: i+x*cnt
  fll = operator.add
  ans = []
  for i in range(1,17):
    lst = LST([0] * i, f, fl, fll, 0, 0)
    lst.update(0, i//2, 1)
    for j in range(i) : lst._apply(j)
    print(lst.seg)
    # debug(lst.cnt)

  # sys.stdout.write("\n".join(map(str, ans)))
sol()