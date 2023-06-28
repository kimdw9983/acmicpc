import importlib, sys, time
from types import ModuleType
from lib.nojam import *

###############
# TODO        
# TC 자동생성

magenta = "\x1b[35;20m"
green = "\x1b[32;20m"
blue = "\x1b[34m"
yellow = "\x1b[33;20m"
red = "\x1b[31;20m"
reset = "\x1b[0m"

def invoke(module: ModuleType):
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
      importlib.reload(module)
    
      print(f"{green}[DONE] {blue}{module.__name__}.py{reset}\t{yellow}CASE {str(tnum)}{reset} elapsed time: {yellow}{time.time() - elapsed}{reset}")
    except (NameError, SyntaxError, StopIteration) as e:
      print(f"{red}[FAIL] {blue}{module.__name__}.py{reset}\t{yellow}CASE {str(tnum)}{reset} elapsed time: {yellow}{time.time() - elapsed}\t{magenta}{type(e).__name__}{reset}")
      # seek()
    init_nprint()
    if fp == prev_fp : #모듈을 실행했는데 파일포인터가 움직이지 않은 경우 -> 종료조건
      return
    

def get_module(name, package=None): #module객체를 실행시키지 않고 가지고 옴
  #https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
  absolute_name = importlib.util.resolve_name(name, package)
  module = sys.modules.get(absolute_name)
  if module: return module

  for finder in sys.meta_path:
    spec = finder.find_spec(absolute_name, None)
    if spec is not None:
      break
  if not spec : return
  module = importlib.util.module_from_spec(spec)
  sys.modules[absolute_name] = module

  return module

try : #필요하면 pre_test.py를 만들것.
  elapsed = time.time()
  import pre_test
  # print(f"{green}[DONE]\t{blue}pre_test.py{reset}, elapsed time: {yellow}{time.time() - elapsed}{reset}")
except :
  pass

try :
  input()
except : 
  pass

for fname in (
              "test", 
              "test2", 
              "test3", 
              "test4",
              "test5",
              "test6",
              ) :
  module = get_module(fname)
  if not module : continue

  seek()
  invoke(module)