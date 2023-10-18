from util import *
import glob, os, re, json, subprocess

SOURCE_DIR = "source"
TESTCASE_DIR = "testcase"

input_testcase = []
output_testcase = []
def parse_acmicpc(file, is_input) :
  with open(file, 'r') as f :
    stream = f.read()
    if not stream: return
    pattern = re.compile(r'(?<!\\)next|^\s*;;.*$', re.MULTILINE)
    TC = pattern.split(stream)
    TC = [s.lstrip('\n').encode() for s in TC if s.lstrip('\n')]
    
    if is_input :
      input_testcase.extend(TC)
    else :
      output_testcase.extend(TC)

for input in glob.glob(f"{TESTCASE_DIR}/input.acmicpc") :
  parse_acmicpc(input, True)
for output in glob.glob(f"{TESTCASE_DIR}/output.acmicpc") :
  parse_acmicpc(output, False)

def parse_standard(file, is_input) :
  with open(file, 'r') as f :
    TC = f.read()
    if not TC: return
    if is_input :
      input_testcase.append(TC.encode())
    else :
      output_testcase.append(TC.encode())

for input in glob.glob(f"{TESTCASE_DIR}/*.in") :
  parse_standard(input, True)
for output in glob.glob(f"{TESTCASE_DIR}/*.out") :
  parse_standard(output, False)

import time
for dir in glob.glob(f"{SOURCE_DIR}/*.py") : 
  for idx, TC in enumerate(input_testcase) :
    metadata = {
      "source": dir, 
      "index": idx
    }
    metadata = json.dumps(metadata)

    env = os.environ.copy()
    env.update({ 
      "PYDEVD_DISABLE_FILE_VALIDATION": "1"
    })
    start_time = time.time()
    proc = subprocess.Popen(["python", '-m', "wrapper", metadata], stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=env)
    stdout, stderr = proc.communicate(input=TC)
    elapsed = int((time.time() - start_time) * 1000)

    output, result = stdout.decode().split("b'\\x1e'")
    if output : print(output)
    print(result)