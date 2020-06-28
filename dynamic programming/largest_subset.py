def largestSubset(arr):
    # sort array in ascending order
    arr.sort()

    # declare length variable
    n = len(arr)

    # declare array to save number of frequency
    freq = [0] * n

    # last element is the largest
    # it's freq is 1
    freq[n-1] = 1

    # fill freq for smaller elements 
    for index in range(n-2, -1, -1):
        # find all multiplies for freq[index]
        mxm = 0
        el = arr[index]
        for sub in range(index+1, n):
            subEl = arr[sub]
            if subEl % el == 0:
                mxm = max(mxm, freq[sub])
        freq[index] = 1 + mxm

    return max(freq)

largestSubset([1, 5, 3, 16, 18])
