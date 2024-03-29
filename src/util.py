bold = "\x1b[1m"
magenta = "\x1b[35;20m"
green = "\x1b[32;20m"
blue = "\x1b[34m"
yellow = "\x1b[33;20m"
red = "\x1b[31;20m"
reset = "\x1b[0m"

METADATA_SEPARATOR = '\x1e' #record separator
END_OF_TESTCASE = '\x04' #end of transmission
COMPILE_ERROR_SIGNAL = '\x1F' #unit separator
RUNTIME_ERROR_SIGNAL = '\x1D' #group separator
INPUT_NOT_CONSUMED = '\x1C' #file separator

TESTS_DIR = "tests"
TESTCASE_DIR = "testcases"

import sys
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
  for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
    if abs(num) < 1024.0:
      return f"{num:3.1f}{unit}{suffix}"
    num /= 1024.0
  return f"{num:.1f}Yi{suffix}"

import importlib.util, sys
def get_module(name, location=None, package=None): #module객체를 실행시키지 않고 가지고 옴
  absolute_name = importlib.util.resolve_name(name, package)
  spec = importlib.util.spec_from_file_location(name, location)
  if not spec : return False
  module = importlib.util.module_from_spec(spec)
  sys.modules[absolute_name] = module

  return spec, module