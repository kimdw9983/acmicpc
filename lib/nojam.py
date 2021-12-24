import sys
import time
import datetime

f = open("input") #파일의 iterator를 공유한다.

class hack_open :
  def __init__(self) :
    self.iter = iter(f)

  def __call__(self, *junk) :
    try :
      return self.iter.__next__()
    except StopIteration :
      None

class hack_input(hack_open) :
  def __call__(self, *junk) :
    try :
      return self.iter.__next__()#[:-1] #줄바꿈문자 제거
    except StopIteration :
      None

__builtins__['f'] = f
sys.stdin.readline = hack_open()
__builtins__['input'] = hack_input()
#####################################################
def NULL(Um=None,Jun=None,Sik=None,*Is,**alive) :
  return 
__builtins__['NULL'] = NULL
def no_print() :
  __builtins__['print'] = NULL
#####################################################
perf_counter = time.perf_counter()
process_time = time.process_time()
def benchmark() :
  global perf_counter, process_time
  print(f'perf_counter : {time.perf_counter() - perf_counter}\nprocess_time : {time.process_time()- process_time}')

__builtins__['benchmark'] = benchmark
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

  print(f"BEFORE : {before_memory} B")
  print(f"AFTER  : {after_memory} B")
  #print(f"LEFT   : {left_memory} B")

Repl.it의 가상환경에는 별로 도움되지않는
"""
def memory(x) : #단위:Byte
  print(sys.getsizeof(x))

__builtins__['memory'] = memory
#####################################################
Repl_now = datetime.datetime.now()
Korea_now = Repl_now + datetime.timedelta(hours=9)
fname = Korea_now.strftime("%Y%m%d_%H:%M:%S")
  
def fprint(*s, sep=" ", end="\n") :
  line = ""
  for w in s :
    line += w.__str__()+sep
  line += end
  with open("output/"+fname, "a") as f:
    f.write(line)

__builtins__['fprint'] = fprint
###################################################

###################################################
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
##################################################
"""
import resource
  
def limit_memory(maxsize):
  soft, hard = resource.getrlimit(resource.RLIMIT_AS)
  print(soft, hard)
  #resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))

MB = 1024 * 1024
limit_memory(256 * MB)

__builtins__['max_memory'] = limit_memory
"""
##################################################
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