from lib.nojam import *
from importlib import reload

#no_print() #print함수를 아무것도 하지 않는 함수로 바꾸기.
#reload(test)

def next_case() :
  f.seek(0)
  reload(test)

import test