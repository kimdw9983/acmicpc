from util import * #여러번 해야할 수 있음
import json, os, pathlib, psutil, time, io, datetime, traceback

args = json.loads(sys.argv[1]) #metadata
# TODO: depend wheather traceback mode or not
sys.tracebacklimit = 1

source: str = args['source']
abspath = str(pathlib.Path(__file__).parent.resolve())
path = os.path.join(abspath, "source")
fname = source.split("\\")[-1].split(".")[0]
spec, module = get_module(fname, os.path.join(path, fname + ".py"))
if not module: raise Exception("module not found")

tc_index = args['index']
now = datetime.datetime.now()
fname = now.strftime("%Y_%m_%d_%H_%M_%S") + f"_{fname}_TC{tc_index}.txt"
def fprint(*args, filename=fname, sep=" ", end="\n"): 
  with open("output/"+filename, "a+") as f:
    f.write(sep.join(map(str, args)) + end)
__builtins__.fprint = fprint

class hack_bytesIO(io.BytesIO) :
  def readline(self) :
    return sys.stdin.buffer.readline()
io.BytesIO = hack_bytesIO

def debug(*args, **kwargs) :
  args = [f"{reset}{magenta}"] + list(args) + [reset]
  print(*args, **kwargs)
__builtins__.debug = debug

current_process = psutil.Process()
before_memory = current_process.memory_info()
start_time = time.time()
try :
  spec.loader.exec_module(module)
except SyntaxError as e :
  print(COMPILE_ERROR_SIGNAL)
  traceback.print_exc(1) #also prints PEP-657 – Include Fine Grained Error Locations in Tracebacks 
  sys.exit(0)
elapsed = int((time.time() - start_time) * 1000)

print(METADATA_SEPARATOR) # let judge know trailing data is not going to be judge.
after_memory = current_process.memory_info()

print(f'메모리: {(after_memory.rss - before_memory.rss) // 1024}KB, 시간: {elapsed}ms')