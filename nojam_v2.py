from util import *
import glob, os, re, json, subprocess, collections, psutil

SOURCE_DIR = "source"
TESTCASE_DIR = "testcase"

input_testcase = collections.deque()
output_testcase = []
def parse_acmicpc(file, is_input) :
  with open(file, 'r') as f :
    stream = f.read()
    if not stream: return
    pattern = re.compile(r'(?<!\\)next|^\s*;;.*$', re.MULTILINE)
    TC = pattern.split(stream)
    TC = [s.lstrip('\n') for s in TC]
    
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
      input_testcase.append(TC)
    else :
      output_testcase.append(TC)

for input in glob.glob(f"{TESTCASE_DIR}/*.in") :
  parse_standard(input, True)
for output in glob.glob(f"{TESTCASE_DIR}/*.out") :
  parse_standard(output, False)

for dir in glob.glob(f"{SOURCE_DIR}/*.py") : 
  metadata = {"source": dir}
  metadata = json.dumps(metadata)

  env = os.environ.copy()
  env.update({ 
    "PYDEVD_DISABLE_FILE_VALIDATION": "1"
  })

  proc = subprocess.Popen(["python", '-m', "wrapper", metadata], stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=env)
  ps = psutil.Process(proc.pid)
  stdout, stderr = proc.communicate()
  print(stdout.decode(), stderr)
  