from util import *
import glob, os, re, json, subprocess

input_testcase = []
output_testcase = []
def parse_acmicpc(file, is_input) :
  with open(file, 'rb') as f : #parse stream in bytes
    stream = f.read()
    if not stream: return
    pattern = re.compile(rb'(?<!\\)next|^\s*;;.*$', re.MULTILINE)
    TC = pattern.split(stream)
    TC = [s.lstrip(b'\n') for s in TC if s.lstrip(b'\n')]
    
    if is_input :
      input_testcase.extend(TC)
    else :
      output_testcase.extend(TC)

for input in glob.glob(f"{TESTCASE_DIR}/input.acmicpc") :
  parse_acmicpc(input, True)
for output in glob.glob(f"{TESTCASE_DIR}/output.acmicpc") :
  parse_acmicpc(output, False)

def parse_standard(file, is_input) :
  with open(file, 'rb') as f :
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

#if no input testcases, put dummy to test the code anyway.
if not input_testcase :
  input_testcase.append(b"")

env = os.environ.copy()
# env.update({ 
#   "PYDEVD_DISABLE_FILE_VALIDATION": "1"
# })

metadata = []
streams: list[bytes] = []
for dir in glob.glob(f"{TESTS_DIR}/*.py") : 
  for idx, stream in enumerate(input_testcase) :
    metadata.append(json.dumps({
      "source": dir, 
      "index": idx,
    }).encode())
    streams.append(stream)

with subprocess.Popen(
  ["pypy", "-Xfrozen_modules=off", '-m', "src.wrapper"], 
  env=env, 
  stdin=subprocess.PIPE, 
  stdout=subprocess.PIPE,
  stderr=subprocess.PIPE,
) as proc :
  while metadata :
    print(metadata, streams)
    proc.stdin.write(metadata.pop() + b"\n") #input of metadata: find source file's directory and indicates which testcase is it.
    proc.stdin.flush()

    proc.stdin.write(streams.pop() + b"\n") #input of testcase
    proc.stdin.flush()
    
    error = None
    result_flag = False
    result = []
    errors = []
    while line := proc.stdout.readline() :
      match line :
        case s if s[0] == ord(END_OF_TESTCASE) :
          break
        case s if s[0] == ord(METADATA_SEPARATOR) :
          result_flag = True
        case s if s[0] == ord(COMPILE_ERROR_SIGNAL) :
          error = "Compile Error"
          break
        case s if s[0] == ord(RUNTIME_ERROR_SIGNAL) :
          error = "Runtime Error"
          break
        case s if error :
          errors.append(s)
        case s if result_flag :
          result.append(s)
        case s :
          sys.stdout.write(s.decode())

    #if input buffer is still remaining, flush it.
    
    
    if error :
      print(f"{red}[{error}]{reset}")
      print(b"\n".join(errors).decode())
    
    if result : #채점 모드일땐 AC, WA 판단 그 외에는 DONE 출력
      print(f"{green}[DONE]{reset}", end=" ")
      print(b"\n".join(result).decode())

  # print(f"{green}[INFO]{reset} Testcases are all done. Terminating")
  proc.terminate()
  try:
    proc.wait(timeout=0.2)
  except subprocess.TimeoutExpired:
    proc.kill()
    proc.wait()