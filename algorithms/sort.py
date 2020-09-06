def insertionSort(arr):
    for i in range(1, len(arr)):
        el = arr[i]
        index = i
        while arr[index-1] > el and index > 0:
            arr[index] = arr[index-1]
            index -= 1
        arr[index] = el

def mergeSort(arr):
    if len(arr) < 2:
        return

    middle = len(arr) // 2
    L = arr[middle:]
    R = arr[:middle]

    mergeSort(L)
    mergeSort(R)

    li = ri = currentIndex = 0
    
    while li < len(L) and ri < len(R):
        if L[li] < R[ri]:
            arr[currentIndex] = L[li]
            li += 1

        else:
            arr[currentIndex] = R[ri]
            ri += 1

        currentIndex += 1

    while li < len(L):
        arr[currentIndex] = L[li]
        li += 1
        currentIndex += 1

    while ri < len(R):
        arr[currentIndex] = R[ri]
        ri += 1
        currentIndex += 1

def quickSort(arr, low, high):
    if low >= high:
        return

    def partition(arr, low, high):
        pivot = arr[high]
        index = low

        for i in range(low, high):
            if arr[i] < pivot:
                arr[i], arr[index] = arr[index], arr[i]
                index += 1

        arr[index], arr[high] = arr[high], arr[index]
        return index

    pi = partition(arr, low, high)
    quickSort(arr, low, pi-1)
    quickSort(arr, pi+1, high)
if __name__ == "__main__":
    arr = [9, 6, 8, 1, 5, 7, 3, 4, 2, 2, 5, 6]
    quickSort(arr, 0, len(arr)-1)
    print(arr)