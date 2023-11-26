numbers = [1, 4, 7, 2, 5, 9, 0, 3, 6, 8]

def counting_sort(arr):
    maximum = max(arr) + 1
    indicies = [0] * maximum
    sorted_arr = [0] * len(arr)
    for el in arr:
        indicies[el] += 1
    for index in range(1, maximum):
        indicies[index] += indicies[index - 1]
    for val in arr:
        last_index = indicies[val]
        sorted_arr[last_index - 1] = val
        indicies[val] -= 1
    return sorted_arr


print(counting_sort(numbers))