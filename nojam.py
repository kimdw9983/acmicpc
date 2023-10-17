from util import *
__builtins__['size'] = lambda x: _print(sizeof_fmt(get_size(x)))
__builtins__['get_size'] = lambda x: _print(sizeof_fmt(get_size(x)))

import importlib.util, sys, time
from types import ModuleType
def get_module(name, location=None, package=None): #module객체를 실행시키지 않고 가지고 옴
  #https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
  absolute_name = importlib.util.resolve_name(name, package)
  module = sys.modules.get(absolute_name)
  if module: return None, module
  
  spec = importlib.util.spec_from_file_location(name, location)
  # for finder in sys.meta_path:
  #   spec = finder.find_spec(absolute_name, None)
  #   if spec is not None:
  #     break
  if not spec : return False
  module = importlib.util.module_from_spec(spec)
  sys.modules[absolute_name] = module

  return spec, module

def invoke(module: ModuleType, fname: str, spec=None):
  global fp
  tnum = 1
  
  while True:
    try:
      first_fp = fp
      input() #f가 비었으면 예외가 발생함.
    except StopIteration:
      return

    if first_fp :
      tnum += 1
    seek(first_fp)

    prev_fp = first_fp
    elapsed = time.time()
    try :
      judge_status[fname] = "AC"
      spec.loader.exec_module(module)
      status = judge_status[fname]
      is_ac = status != "WA"
      _print(f"{green if is_ac else red}[{status: ^4}] {blue}{module.__name__}.py{reset}\t{yellow}CASE {str(tnum)}{reset} elapsed time: {yellow}{time.time() - elapsed}{reset}")
    except (NameError, SyntaxError, StopIteration) as e:
      if type(e) is UnboundLocalError : #UnboundedLocalError는 NameError의 부분 집합이지만 raise하기에 충분함
        raise e
      _print(f"{red}[FAIL] {blue}{module.__name__}.py{reset}\t{yellow}CASE {str(tnum)}{reset} elapsed time: {yellow}{time.time() - elapsed}\t{magenta}{type(e).__name__}{reset}")
      # seek()
    init_nprint()
    if fp == prev_fp : #모듈을 실행했는데 파일포인터가 움직이지 않은 경우 -> 종료조건
      return
#####################################################
import sys, datetime, os, io
f = open("testcase/input.acmicpc", 'r+', encoding="utf-8", errors="ignore") #파일의 iterator를 공유한다.

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
#####################################################
def debug(*args, **kwargs) :
  args = [f"{yellow}{reset}{magenta}"] + list(args) + [reset]
  _print(*args, **kwargs)
__builtins__['debug'] = debug
fo = open("testcase/output.acmicpc", 'r+', encoding="utf-8", errors="ignore") if os.stat("testcase/output.acmicpc").st_size != 0 else None

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
        if s.rstrip() in ("\\next"):  continue #필요한진 모르겠음
        return s
      else :
        raise StopIteration

foi = fo_iter()
judge_status = {}
def set_current_file(file_name) :
  global current_file
  current_file = file_name

def init_judge() :
  if not fo: return
  fo.seek(0)

def make_line(*args, **kwargs) :
  sep = kwargs.get('sep', ' ')
  end = kwargs.get('end', '\n')

  line = sep.join(map(str, list(args))) + end
  _write(line)
  return line

def judge_print(*args, **kwargs) :
  line = make_line(*args, **kwargs)
  judge_line(line)

def judge_write(line: str):
  _write(line)
  judge_line(line)

def judge_line(line: str) : #TODO: fstring으로 개행문자가 포함된 line이 들어오면 한줄로 인식하는 문제
  if fo :
    try :
      answer = foi.read()
    except :
      answer = ""

    if line.strip() != answer.strip() : 
      debug(red+answer.strip())
      judge_status[current_file] = "WA"
  else :
    judge_status[current_file] = "DONE"

_print = __builtins__['_print'] = make_line
_write = sys.stdout.write
sys.stdout.write = judge_write
__builtins__['print'] = judge_print
##########################################################
import json
def pprint(obj, **kwargs) :
  """2차원 이상의 배열을 보기좋게 출력"""
  # from numpy import set_printoptions, array
  # set_printoptions(linewidth = 999)
  # _print(array(obj, copy=False, dtype=object, **kwargs), end="\n\n")
  output = json.dumps(obj, ensure_ascii=False, check_circular=False)
  output = output.replace("],", "],\n").replace("],\n\n", "],\n").replace("[[", "[\n[").replace("]]", "]\n]")
  debug(output, end="\n", **kwargs)

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

import json
def fprint(*s, sep=" ", end="\n") :
  """출력을 output/timestamp의 형식의 파일으로 저장"""
  timestamp = datetime.datetime.now()
  fname = timestamp.strftime("%Y_%m_%d_%H_%M_%S")

  x = json.dump(s)

  line = f"{sep.join(x)}{end}"
  with open("output/"+fname, "a") as f:
    f.write(line)
__builtins__['fprint'] = fprint

# try :
#   elapsed = time.time()
#   current_file = "pre_test"
#   import pre_test
#   # _print(f"{green}[DONE]\t{blue}pre_test.py{reset}, elapsed time: {yellow}{time.time() - elapsed}{reset}")
# except ModuleNotFoundError:
#   pass

try :
  input()
except : 
  raise

import glob, pathlib
for s in glob.glob("source/*.py") : 
  abspath = str(pathlib.Path(__file__).parent.resolve())
  path = os.path.join(abspath, "source")
  fname = s.split("\\")[-1].split(".")[0]
  spec, module = get_module(fname, os.path.join(path, fname + ".py"))
  if not module : continue

  seek()
  set_current_file(fname)
  init_judge()
  invoke(module, fname, spec)