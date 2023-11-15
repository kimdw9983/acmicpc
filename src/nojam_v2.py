from util import *
import glob, os, re, json, subprocess

input_testcase: list[bytes] = []
output_testcase: list[bytes] = []
def parse_acmicpc(file, is_input) :
  res = input_testcase if is_input else output_testcase
  with open(file, 'rb') as f : #parse stream in bytes
    stream = f.read()
    if not stream: return
    pattern = re.compile(rb'(?<!\\)next|^\s*;;.*$', re.MULTILINE)
    TC = pattern.split(stream)
    TC = [s.lstrip() for s in TC if s.lstrip()]
    
    res.extend(TC)

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
streams = []
for dir in glob.glob(f"{TESTS_DIR}/*.py") : 
  for idx, stream in enumerate(input_testcase) :
    metadata.append(json.dumps({
      "source": dir, 
      "index": idx,
    }).encode())
    streams.append(stream)
metadata.reverse()
streams.reverse()

with subprocess.Popen(
  [sys.argv[1], "-B", "-Xfrozen_modules=off", '-m', "src.wrapper"], 
  env=env, 
  stdin=subprocess.PIPE, 
  stdout=subprocess.PIPE,
  stderr=subprocess.PIPE,
) as proc :
  while metadata :
    proc.stdin.write(metadata.pop() + b"\n")
    proc.stdin.write(streams.pop() + b"\n")
    proc.stdin.flush() 
    #IPC의 관점에서, flush()는 데이터를 보내기로 확정하는 것과 같다. git의 commit과 비슷하다.
    #터미널에 입력창이 떴을 때 입력을 마치기 전까지 무기한 대기하는 것을 생각하면 된다.
    
    error = None
    warning = set()
    result_flag = False
    result = []
    errors = []
    while line := proc.stdout.readline() :
      match line :
        case s if s[0] == ord(END_OF_TESTCASE) :
          break
        case s if s[0] == ord(METADATA_SEPARATOR) :
          result_flag = True
        case s if s[0] == ord(INPUT_NOT_CONSUMED) :
          warning.add("Input has not fully consumed")
        case s if s[0] == ord(COMPILE_ERROR_SIGNAL) :
          error = "Compile Error"
        case s if s[0] == ord(RUNTIME_ERROR_SIGNAL) :
          error = "Runtime Error"
        case s if result_flag :
          result.append(s.rstrip())
        case s if error :
          errors.append(s.rstrip())
        case s :
          sys.stdout.write(s.decode())
    
    status = f"{green}[DONE]{reset}" #(AC, WA, TLE, MLE, RE, CE, IE, OLE, SE)
    if warning :
      status = f"{yellow}[WARN]"
      print(yellow + '\n'.join(warning) + reset)

    if error :
      status = f"{red}[FAIL]{reset}"
      print(b"\n".join(errors).decode())
      print(f"{red}{error}{reset}")
    
    if result : 
      print(f"{status}{reset} {sys.argv[1]}", end=" ")
      print(b"\n".join(result).decode())

  # print(f"{green}[INFO]{reset} Testcases are all done. Terminating")
  proc.terminate()
  try:
    proc.wait(timeout=0.2)
  except subprocess.TimeoutExpired:
    proc.kill()
    proc.wait()