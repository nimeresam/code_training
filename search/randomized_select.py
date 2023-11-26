
def partition(arr, left, right):
    index = left - 1
    pointer = left
    value = arr[right]
    while pointer < right:
        if arr[pointer] < value:
            index += 1
            arr[index], arr[pointer] = arr[pointer], arr[index]
        pointer += 1
    index += 1
    arr[index], arr[right] = arr[right], arr[index]
    return index

def randomizedSelect(arr, left, right, index):
    if left == right:
        return arr[left]
    pivot = partition(arr, left, right)
    if pivot == index:
        return arr[pivot]
    if index < pivot:
        return randomizedSelect(arr, left, pivot - 1, index)
    return randomizedSelect(arr, pivot + 1, right, index)

third = randomizedSelect([9, 1, 4, 3, 5, 6, 8, 0, 2, 7], 0, 9, 6)
print(third)
    