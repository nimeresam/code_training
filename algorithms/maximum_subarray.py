stocks = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]

def maximum_subarray_bf(arr):
    diffs = [0] * (len(arr) - 1)

    for idx in range(len(diffs)):
        diffs[idx] = arr[idx + 1] - arr[idx]
    
    mx = 0
    start = 0
    end = 0
    for oi in range(len(diffs)):
        current_max = diffs[oi]
        current_end = oi
        total = diffs[oi]
        for ii in range(oi + 1, len(diffs)):
            total += diffs[ii]
            if total > current_max:
                current_max = total
                current_end = ii
        if current_max > mx:
            mx = current_max
            start = oi
            end = current_end
    return [mx, start, end]

def __find_maximum(arr, start, end):
    element = start
    value = arr[start]
    total = arr[start]
    for index in range(start + 1, end + 1):
        total += arr[index]
        if total > value:
            value = total
            element = index
    return [element, value]

def __find_maximum_crossing_subarray(arr, low, mid, high):
    [low_el, left_max] = __find_maximum(arr, low, mid)
    [high_el, right_max] = __find_maximum(arr, mid + 1, high)
    return [low_el, high_el, left_max + right_max]

def maximum_subarray_dc(arr, low, high):
    if low == high:
        return [low, high, arr[low]]
    
    mid = (high + low) // 2
    [left_low, left_high, left_max] = maximum_subarray_dc(arr, low, mid)
    [right_low, right_high, right_max] = maximum_subarray_dc(arr, mid + 1, high)
    [cross_low, cross_high, cross_max] = __find_maximum_crossing_subarray(arr, low, mid, high)

    if left_max >= right_max and left_max >= cross_max:
        return [left_low, left_high, left_max]
    if right_max >= left_max and right_max >= cross_max:
        return [right_low, right_high, right_max]
    return [cross_low, cross_high, cross_max]

diffs = [0] * (len(stocks) - 1)

for idx in range(len(diffs)):
    diffs[idx] = stocks[idx + 1] - stocks[idx]

[val, start, end] = maximum_subarray_dc(diffs, 0, len(diffs) -1)
print(val)