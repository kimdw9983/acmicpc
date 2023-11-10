from src.util import *
import json, os, pathlib, psutil, time, io, datetime, traceback

# args = json.loads(sys.argv[1]) #metadata
# TODO: depend wheather traceback mode or not
sys.tracebacklimit = 2
default_output_name=""

def fprint(*args, filename=default_output_name, sep=" ", end="\n"): 
  with open(sys.path[0] + "output/"+filename, "a+") as f:
    f.write(sep.join(map(str, args)) + end)

class hack_bytesIO(io.BytesIO) :
  def readline(self) :
    return sys.stdin.readline().encode()
io.BytesIO = hack_bytesIO

def debug(*args, **kwargs) :
  args = [f"{reset}{magenta}"] + list(args) + [reset]
  print(*args, **kwargs)

__builtins__.fprint = fprint
__builtins__.size = lambda x: sizeof_fmt(get_size(x))
__builtins__.get_size = lambda x: sizeof_fmt(get_size(x))
__builtins__.debug = debug

CURRENT_PROCESS = psutil.Process()

if __name__ == "__main__" :
  while metadata := input() :
    metadata = json.loads(metadata)
    source: str = metadata['source']
    abspath = str(pathlib.Path(__file__).parent.parent.resolve())
    tc_index = metadata['index']
    path = os.path.join(abspath, TESTS_DIR)
    fname = source.split("\\")[-1].split(".")[0]
    default_output_name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + f"_{default_output_name}_TC{tc_index}.txt"
    spec, module = get_module(fname, os.path.join(path, fname + ".py"))

    if not module: raise Exception("module not found")

    try :
      before_memory = CURRENT_PROCESS.memory_info()
      start_time = time.time()
      spec.loader.exec_module(module)
    except (SyntaxError, FileNotFoundError) as e : #TODO: add all the cases that can be considered as compile error
      print(COMPILE_ERROR_SIGNAL)
      traceback.print_exc(1) #also prints PEP-657 – Include Fine Grained Error Locations in Tracebacks 
    except (SystemExit, OSError) as e : #TODO: capture debugger shutdown(exit Code 0)
      pass
    except Exception as e : #probably runtime error
      print(RUNTIME_ERROR_SIGNAL)
      traceback.print_exc(1)

    while sys.stdin.tell() : #There's input stream remaining but not processed. Consume all before next testcase.
      sys.stdin.readline()

    elapsed = int((time.time() - start_time) * 1000)
    print(METADATA_SEPARATOR) # let judge know trailing data is not going to be judge.
    after_memory = CURRENT_PROCESS.memory_info()
    del spec, module

    print(f'{blue}MEMORY:{reset} {(after_memory.rss - before_memory.rss) // 1024}KB, {blue}ELAPSED:{reset} {elapsed}ms')
    print(END_OF_TESTCASE, flush=True)