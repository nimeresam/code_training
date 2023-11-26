
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

print(binarySearch(5, [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ] ))