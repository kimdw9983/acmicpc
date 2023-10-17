from util import *
__builtins__['size'] = lambda x: sizeof_fmt(get_size(x))
__builtins__['get_size'] = lambda x: sizeof_fmt(get_size(x))



# Import and run the target script
import time
start_time = time.time()
#run script (this could fail)
###
elapsed = int(time.time() - start_time * 1000)

# print(f'언어: , 메모리: NNNNNN, 시간: {elapsed}')