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
import sys
def memory(x) : #단위:Byte
  print(sys.getsizeof(x))

__builtins__['memory'] = memory
##################################################
# Available only in Linux
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