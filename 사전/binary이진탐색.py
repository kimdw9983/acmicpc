def binary_search(arr, x: int) : #data는 정렬돼있어야 함
  start = 0
  end = len(arr) - 1

  while start <= end :
    mid = (start + end) // 2
    if arr[mid] == x :
      return mid
    elif arr[mid] < x :
      start = mid + 1
    else :
      end = mid - 1
  return -1

def decision(param): #결정 함수
  pass
    
#high : 구간 최대값 + 1
def parametric_search_find_highest(lo,hi): 
  while lo + 1 < hi:
    mid = (lo + hi) // 2
    if decision(mid):
      lo = mid #최소값 구할땐 hi = mid
    else:
      hi = mid #vise versa
  return lo #최소값 구할땐 hi

#low : 구간 최소값 - 1
def parametric_search_find_lowest(lo,hi): 
  while lo + 1 < hi:
    mid = (lo + hi) // 2
    if decision(mid):
      hi = mid #최소값 구할땐 hi = mid
    else:
      lo = mid #vise versa
  return hi #최소값 구할땐 hi