from lib.nojam import *
from importlib import reload

#no_print() #print함수를 아무것도 하지 않는 함수로 바꾸기.
#reload(test)

def next_case() :
	f.seek(0) #파일포인터를 처음지점으로 옮긴다
	reload(test)

import test
f.seek(0)
import test2