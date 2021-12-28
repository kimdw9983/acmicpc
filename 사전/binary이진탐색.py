def binary_search(arr, x: int):  #data는 정렬돼있어야 함
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def decision(param):  #결정 함수
    pass

#high : 구간 최대값 + 1
def parametric_search_find_highest(low, high):
    while low + 1 < high:
        mid = (low + high) // 2
        if decision(mid):
            low = mid
        else:
            high = mid
    return low

#low : 구간 최소값 - 1
def parametric_search_find_lowest(low, high):
    while low + 1 < high:
        mid = (low + high) // 2
        if decision(mid):
            high = mid
        else:
            low = mid
    return high
