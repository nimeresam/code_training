
# Online Python - IDE, Editor, Compiler, Interpreter
unsorted = [2, 6, 5, 1, 0, 3, 7, 8, 4]

def quickSort(arr, left, right):
    if left >= right:
        return
    def partition(arr, left, right):
        index = left - 1
        pointer = left
        value = arr[right]
        while pointer < right:
            if arr[pointer] < value:
                index += 1
                arr[pointer], arr[index] = arr[index], arr[pointer]
            pointer += 1
        index += 1
        arr[right], arr[index] = arr[index], arr[right]
        return index
    pivot = partition(arr, left, right)
    quickSort(arr, left, pivot - 1)
    quickSort(arr, pivot + 1, right)

def quickSortNoDuplicates(arr, left, right):
    if left >= right:
        return
    def partition(arr, left, right):
        value = arr[right]
        pivot_start = left - 1

        pointer_start = left
        pointer_end = right
        while pointer_start < pointer_end:
            if arr[pointer_start] == value:
                pointer_end -= 1
                arr[pointer_start], arr[pointer_end] = arr[pointer_end], arr[pointer_start]
            else:
                if arr[pointer_start] < value:
                    pivot_start += 1
                    arr[pointer_start], arr[pivot_start] = arr[pivot_start], arr[pointer_start]
                pointer_start += 1
        
        duplicates = right - pointer_end + 1
        pivot_end = pivot_start + duplicates
        pivot_start += 1
        
        index = pivot_start
        while pointer_end <= right:
            arr[index], arr[pointer_end] = arr[pointer_end], arr[index]
            index += 1
            pointer_end += 1
        return [pivot_start, pivot_end]
    [pivot_start, pivot_end] = partition(arr, left, right)
    quickSort(arr, left, pivot_start - 1)
    quickSort(arr, pivot_end + 1, right)

quickSort(unsorted, 0, len(unsorted) - 1)