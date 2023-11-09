from src.util import *
import json, os, pathlib, psutil, time, io, datetime, traceback

args = json.loads(sys.argv[1]) #metadata
# TODO: depend wheather traceback mode or not
sys.tracebacklimit = 2
FNAME=""

def fprint(*args, filename=FNAME, sep=" ", end="\n"): 
  with open(sys.path[0] + "output/"+filename, "a+") as f:
    f.write(sep.join(map(str, args)) + end)

class hack_bytesIO(io.BytesIO) : #소스 코드의 stdin 버퍼가 아닌, wrapper의 stdin 버퍼를 사용
  def readline(self) :
    return sys.stdin.buffer.readline()
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
  while True :
    metadata = input()
    if not metadata : exit()

    metadata = json.loads(metadata)
    source: str = args['source']
    abspath = str(pathlib.Path(__file__).parent.parent.resolve())
    path = os.path.join(abspath, TESTS_DIR)
    FNAME = source.split("\\")[-1].split(".")[0]
    spec, module = get_module(FNAME, os.path.join(path, FNAME + ".py"))
    if not module: raise Exception("module not found")

    tc_index = args['index']
    now = datetime.datetime.now()
    FNAME = now.strftime("%Y_%m_%d_%H_%M_%S") + f"_{FNAME}_TC{tc_index}.txt"
    before_memory = CURRENT_PROCESS.memory_info()
    start_time = time.time()
    try :
      spec.loader.exec_module(module)
    except (SyntaxError, FileNotFoundError) as e :
      print(COMPILE_ERROR_SIGNAL)
      traceback.print_exc(1) #also prints PEP-657 – Include Fine Grained Error Locations in Tracebacks 
      sys.exit(0)
    #TODO: capture debugger shutdown(exit Code 0)

    elapsed = int((time.time() - start_time) * 1000)
    del spec, module

    print(METADATA_SEPARATOR) # let judge know trailing data is not going to be judge.
    after_memory = CURRENT_PROCESS.memory_info()

    print(f'{blue}MEMORY:{reset} {(after_memory.rss - before_memory.rss) // 1024}KB, {blue}ELAPSED:{reset} {elapsed}ms')
    print(END_OF_TESTCASE)