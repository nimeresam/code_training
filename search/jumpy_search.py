import math

def jumpSearch(el, arr):
    n = len(arr)
    step = int(math.sqrt(n))

    prev = 0

    while arr[min(step, n-1)] < el:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < el:
        prev += 1

        if prev == min(step, n):
            return -1

    if arr[prev] == el:
        return prev
    return -1
