from binary_search import binarySearch

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