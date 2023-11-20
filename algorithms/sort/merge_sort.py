
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


arr = [9, 6, 8, 1, 5, 7, 3, 4, 2, 2, 5, 6]
mergeSort(arr)
print(arr)