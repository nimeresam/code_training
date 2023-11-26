numbers = [1, 4, 7, 2, 5, 9, 0, 3, 6, 8]

def insertionSort(arr):
    for i in range(1, len(arr)):
        el = arr[i]
        index = i
        while arr[index-1] > el and index > 0:
            arr[index] = arr[index-1]
            index -= 1
        arr[index] = el

insertionSort(numbers)
print(numbers)