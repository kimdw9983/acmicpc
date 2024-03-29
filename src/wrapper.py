from src.util import *
import json, os, pathlib, psutil, time, io, datetime, traceback, gc

# TODO: depend wheather traceback mode or not
sys.tracebacklimit = 2
def fprint(*args, filename=None, sep=" ", end="\n"): 
  if not filename:
    filename = OUTPUT_FNAME
  with open("output/"+filename, "a+") as f:
    f.write(sep.join(map(str, args)) + end)

class hack_bytesIO(io.BytesIO) :
  def readline(self) :
    return sys.stdin.readline().encode()
io.BytesIO = hack_bytesIO

def debug(*args, **kwargs) :
  s = f"{reset}{magenta}{list(args).__repr__()[1:-1]}{reset}"
  print(s, **kwargs)

__builtins__.fprint = fprint
__builtins__.size = lambda x: sizeof_fmt(get_size(x))
__builtins__.get_size = lambda x: sizeof_fmt(get_size(x))
__builtins__.debug = debug

CURRENT_PROCESS = psutil.Process()
ABS_PATH = str(pathlib.Path(__file__).parent.parent.resolve())
PATH = os.path.join(ABS_PATH, TESTS_DIR)

if __name__ == "__main__" :
  while metadata := input() :
    metadata = json.loads(metadata)
    source: str = metadata['source']
    tc_index = metadata['index']
    fname = source.split("\\")[-1].split(".")[0]
    OUTPUT_FNAME = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + f"_{fname}_TC{tc_index}.txt"
    spec, module = get_module(fname, os.path.join(PATH, fname + ".py"))
    if not module or not spec: raise Exception("module not found")

    result = []
    result.append(f"{blue}FILE:{reset} {source}")
    result.append(f"{blue}TC:{reset} {tc_index}")
    try :
      start_time = time.time()
      before_memory = CURRENT_PROCESS.memory_info()
      spec.loader.exec_module(module)
      after_memory = CURRENT_PROCESS.memory_info()
      elapsed = int((time.time() - start_time) * 1000)

      result.append(f"{blue}MEMORY:{reset} {(after_memory.rss - before_memory.rss) // 1024}KB")
      result.append(f"{blue}TIME:{reset} {elapsed}ms")
    except (SyntaxError, FileNotFoundError) as e : #TODO: add all the cases that can be considered as compile error
      print(COMPILE_ERROR_SIGNAL)
      traceback.print_exc(1, sys.stdout) #also prints PEP-657 – Include Fine Grained Error Locations in Tracebacks 
    except (SystemExit, OSError) as e : #TODO: capture debugger shutdown(exit Code 0)
      pass
    except Exception as e : #probably runtime error
      print(RUNTIME_ERROR_SIGNAL)
      traceback.print_exc(1, sys.stdout)
      raise
    
    if sys.stdin.tell() : 
      # There's input stream remaining but not processed. Consume all before next testcase.
      # Warn if the remaining input was not a whitespace
      # TODO: 반례 - 안읽은게 testcase내의 개행문자일 수 있음
      line = sys.stdin.readline()
      if line.rstrip(): print(INPUT_NOT_CONSUMED)
      sys.stdin.seek(0, os.SEEK_END)

    print(METADATA_SEPARATOR)
    print(" ".join(result))
    del sys.modules[fname], fname, module, spec
    print(END_OF_TESTCASE)