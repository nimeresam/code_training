import math

def binarySearch(el, arr, l, r):
    if l > r:
        return -1
    # find mid 
    mid = l + (r - l) // 2

    if arr[mid] == el:
        return mid
    
    if arr[mid] > el:
        return binarySearch(el, arr, l, mid-1)
    return binarySearch(el, arr, mid+1, r)

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

def exponentialSearch(el, arr):
    if arr[0] == el:
        return 0
    
    n = len(arr)

    i = 1
    while i < n and arr[i] <= el:
        i *= 2

    return binarySearch(el, arr, int(i/2), min(i, n))

if __name__ == "__main__":
    print(exponentialSearch(5, [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ] ))