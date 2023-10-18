from util import * #여러번 해야할 수 있음
import json, os, pathlib, psutil, time, io, datetime

args = json.loads(sys.argv[1]) #metadata

source: str = args['source']
abspath = str(pathlib.Path(__file__).parent.resolve())
path = os.path.join(abspath, "source")
fname = source.split("\\")[-1].split(".")[0]
spec, module = get_module(fname, os.path.join(path, fname + ".py"))
if not module: raise Exception("module not found")

tc_index = args['index']
timestamp = datetime.datetime.now()
fname = timestamp.strftime("%Y_%m_%d_%H_%M_%S") + f"_{fname}_TC{tc_index}.txt"
def fprint(*args, filename=fname, sep=" ", end="\n"): 
  with open("output/"+filename, "a+") as f:
    f.write(sep.join(map(str, args)) + end)
__builtins__.fprint = fprint

class hack_bytesIO(io.BytesIO) :
  def readline(self) :
    return sys.stdin.buffer.readline()
io.BytesIO = hack_bytesIO

current_process = psutil.Process()
before_memory = current_process.memory_info()
start_time = time.time()
spec.loader.exec_module(module)
elapsed = int((time.time() - start_time) * 1000)

print(METADATA_SEPARATOR) # let judge know trailing data is not going to be judge.
after_memory = current_process.memory_info()

print(f'메모리: {(after_memory.rss - before_memory.rss) // 1024} KB, 시간: {elapsed}ms')