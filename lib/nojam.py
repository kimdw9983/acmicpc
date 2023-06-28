magenta = "\x1b[35;20m"
green = "\x1b[32;20m"
blue = "\x1b[34m"
yellow = "\x1b[33;20m"
red = "\x1b[31;20m"
reset = "\x1b[0m"
#####################################################
import sys, datetime, os, io
f = open("input.acmicpc", 'r+', encoding="utf-8", errors="ignore") #파일의 iterator를 공유한다.

class f_iter :
  def __init__(self, *_) :
    self.iter = iter(f)

  def read(self) :
    while True :
      s = f.readline()

      if s :
        if s.startswith(";;") or s.startswith("\\next"): continue #주석 구현
        __builtins__['fp'] = self.iter.tell()
        return s
      else :
        raise StopIteration

class hack_stdin(f_iter):
  def __call__(self, *_) :
    return self.read()
    
class hack_BytesIO(f_iter) :
  def readline(self, *_) :
    return self.read().encode()

class hack_input(f_iter) :
  def __call__(self, *_) :
    return self.read().rstrip()

def seek(i=0) :
  f.seek(i)
  __builtins__['f'] = f
  __builtins__['fp'] = i
seek()

__builtins__['seek'] = seek
sys.stdin.readline = hack_stdin()
__builtins__['input'] = hack_input()
io.BytesIO = hack_BytesIO


def debug(*args, **kwargs) :
  args = [f"{yellow}{reset}{magenta}"] + list(args) + [reset]
  _print(*args, **kwargs)
__builtins__['debug'] = debug
#####################################################
_print = __builtins__['print']
__builtins__['_print'] = _print
fo = open("output.acmicpc", 'r+', encoding="utf-8", errors="ignore") if os.stat("output.acmicpc").st_size != 0 else None

current_file = None
class fo_iter :
  def __init__(self, *_) :
    self.iter = iter(fo) if fo else None

  def read(self) :
    if not self.iter : return
    while True :
      s = fo.readline()
      if s :
        if s.rstrip() in (";;"): continue #주석 구현
        if s.rstrip() in ("\\next"): 
          global case_num
          case_num += 1
          continue
        return s
      else :
        raise StopIteration

foi = fo_iter()
judge_status = {}
def set_current_file(file_name) :
  global current_file, case_num
  current_file = file_name

def init_judge() :
  if not fo: return
  fo.seek(0)

def judge(*args, **kwargs) :
  sep = kwargs.get('sep', ' ')
  end = kwargs.get('end', '\n')
  supress = kwargs.get('supress', False)

  line = sep.join(map(str, list(args))) + end
  if fo :
    try :
      answer = foi.read()
    except :
      answer = None
      pass
    if line.strip() != answer.strip() : 
      judge_status[current_file] = "WA"
    else :
      judge_status[current_file] = "AC"

  if not supress :
    _print(*args, **kwargs)


__builtins__['print'] = judge
#####################################################
"""
import psutil
import os

PID = os.getpid()
current_process = psutil.Process(PID)
before_memory = current_process.memory_info()[1]

def memory() :
  global before_memory
  after_memory = current_process.memory_info()[1]
  #left_memory = after_memory - before_memory #삭제되지 않은 메모리

  _print(f"BEFORE : {before_memory} B")
  _print(f"AFTER  : {after_memory} B")
  #_print(f"LEFT   : {left_memory} B")
"""
def memory(x) : #단위:Byte
  _print(sys.getsizeof(x))

__builtins__['memory'] = memory
#####################################################
#https://help.acmicpc.net/judge/rte/RecursionError
#BOJ의 채점 서버에서 이 값은 1,000으로 되어 있습니다.
sys.setrecursionlimit(1000)
"""
import sys
sys.setrecursionlimit(10**6)
"""
##################################################
#https://stackoverflow.com/questions/492519/timeout-on-a-function-call
import errno
import os
import signal
import functools

class TimeoutError(Exception):
  pass

def timeout(seconds=1, error_message=os.strerror(errno.ETIME)):
  def decorator(func):
    def _handle_timeout(signum, frame):
      raise TimeoutError(error_message)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      signal.signal(signal.SIGALRM, _handle_timeout)
      signal.alarm(seconds)
      try:
        result = func(*args, **kwargs)
      finally:
        signal.alarm(0)
      return result
    return wrapper
  return decorator

__builtins__['timeout'] = timeout

def get_size(obj, seen=None):
  size = sys.getsizeof(obj)
  if seen is None:
    seen = set()
  obj_id = id(obj)
  if obj_id in seen:
    return 0
  seen.add(obj_id)
  if isinstance(obj, dict):
    size += sum([get_size(v, seen) for v in obj.values()])
    size += sum([get_size(k, seen) for k in obj.keys()])
  elif hasattr(obj, '__dict__'):
    size += get_size(obj.__dict__, seen)
  elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
    size += sum([get_size(i, seen) for i in obj])
  return size

def sizeof_fmt(num, suffix="B"):
  for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
    if abs(num) < 1024.0:
      return f"{num:3.1f}{unit}{suffix}"
    num /= 1024.0
  return f"{num:.1f}Yi{suffix}"

__builtins__['size'] = lambda x: _print(sizeof_fmt(get_size(x)))
##################################################
"""
import resource
  
def limit_memory(maxsize):
  soft, hard = resource.getrlimit(resource.RLIMIT_AS)
  _print(soft, hard)
  #resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))

MB = 1024 * 1024
limit_memory(256 * MB)

__builtins__['max_memory'] = limit_memory
"""
##################################################
import math
def _is_prime(n):
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
def is_prime(n) :
  _print(f"{n}은 소수{'맞음 ㅇㅇ' if _is_prime(n) else '아님 ㄴㄴ'}")

#최소공배수
def lcm(m, n) :
  return m*n//math.gcd(m,n)

def divisors(n : int) : #n의 모든 약수 출력 O(n^.5)
  if not n :
    return [0]
  l = []
  for i in range(1, math.isqrt(n) + 1): 
    if not n % i:            
      l.append(i)
      l.append(n//i)
  return l[::2] + l[-3 if l[-1]==l[-2] else -1::-2]

__builtins__['is_prime'] = is_prime
__builtins__['lcm'] = lcm
__builtins__['gcd'] = math.gcd
__builtins__['divisors'] = divisors
##########################################################
def pprint(obj, **kwargs) :
  """2차원 이상의 배열을 보기좋게 출력"""
  from numpy import set_printoptions, array
  set_printoptions(linewidth = 999)
  _print(array(obj, copy=False, dtype=object, **kwargs), end="\n\n")
__builtins__['pprint'] = pprint

nprint_left = None
def nprint(cnt, *args, **kwargs) : 
  """각 case마다 cnt만큼만 _print"""
  global nprint_left
  if nprint_left is None: nprint_left = cnt 
  elif nprint_left == 0 : return

  _print(*args, **kwargs)
  nprint_left -= 1
__builtins__['nprint'] = nprint

def init_nprint():
  global nprint_left
  nprint_left = None

def fprint(*s, sep=" ", end="\n") :
  """출력을 output/timestamp의 형식의 파일으로 저장"""
  timestamp = datetime.datetime.now()
  fname = timestamp.strftime("%Y%m%d_%H:%M:%S")

  line = ""
  for w in s :
    line += w.__str__() + sep
  line += end
  with open("output/"+fname, "a") as f:
    f.write(line)
__builtins__['fprint'] = fprint