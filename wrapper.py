from util import *

import json, os, pathlib, psutil
args = json.loads(sys.argv[1]) #metadata

source: str = args['source']
abspath = str(pathlib.Path(__file__).parent.resolve())
path = os.path.join(abspath, "source")
fname = source.split("\\")[-1].split(".")[0]
spec, module = get_module(fname, os.path.join(path, fname + ".py"))
if not module: exit(1)

language = args.get('language')

current_process = psutil.Process()

# Import and run the target script
import time
before_memory = current_process.memory_info()
start_time = time.time()
spec.loader.exec_module(module)
elapsed = int((time.time() - start_time) * 1000)

print(METADATA_SEPARATOR) # let judge know trailing data is not going to be judge.
after_memory = current_process.memory_info()

print(f'메모리: {(after_memory.rss - before_memory.rss) // 1024} KB, 시간: {elapsed}ms')