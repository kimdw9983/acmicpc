#import test

import importlib, sys
from lib.nojam import *

#no_print() #print함수를 아무것도 하지 않는 함수로 바꾸기.

###############
# TODO        
# TC 자동생성(json방식 input)
# TC에서 오류 발생해도 모든 케이스 출력하는 옵션 추가

def invoke(module):
  global fp
  tnum = 1
  
  while True:
    try:
      first_fp = fp
      input() #f가 비었으면 예외가 발생함.
    except:
      return

    if first_fp :
      tnum += 1
      print("-"*10+"["+module.__name__+".py] CASE "+ str(tnum) +"-"*10)
    seek(first_fp)

    prev_fp = first_fp
    importlib.reload(module)
    
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

try :
  input()
except : 
  pass

for fname in ("pre_test", "test", "test2", "test3") :
  module = get_module(fname)
  if not module : continue

  seek()
  invoke(module)