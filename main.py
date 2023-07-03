from lib.nojam import *

try : #필요하면 pre_test.py를 만들것.
  elapsed = time.time()
  current_file = "pre_test"
  import pre_test
  # _print(f"{green}[DONE]\t{blue}pre_test.py{reset}, elapsed time: {yellow}{time.time() - elapsed}{reset}")
except ModuleNotFoundError:
  pass

try :
  input()
except : 
  raise

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
  set_current_file(fname)
  init_judge()
  invoke(module, fname)