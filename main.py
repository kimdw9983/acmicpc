from lib.nojam import *
#from pre import *
from importlib import reload

#no_print() #print함수를 아무것도 하지 않는 함수로 바꾸기.
#reload(test)


def load_next_case():
	valid = True
	while valid:
		try:
			f.tell()
		except:
			valid = False

		print("\n" + "-" * 10 + "[main.py] NEXT CASE" + "-" * 10 + "\n")
		reload(test)


import test

f.seek(0)  #파일포인터를 처음지점으로 옮긴다
import test2

#load_next_case()
