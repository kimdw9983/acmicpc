data = range(5)

def binary_search(x: int) : #data는 정렬돼있어야 함
  start = 0
  end = len(data) - 1

  while start <= end :
    mid = (start + end) // 2
    if data[mid] == x :
      return mid
    elif data[mid] < x :
      start = mid + 1
    else :
      end = mid - 1
  
  return -1