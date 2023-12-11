def matrix_multiply(first, second):
    def getDimensions(arr):
        rows = len(arr)
        cols = len(arr[0])
        return [rows, cols]
    [fRs, fCs] = getDimensions(first)
    [sRs, sCs] = getDimensions(second)
    if fCs != sRs:
        raise "Incompaticble"

    arr = [[0 for _ in range(sCs)] for _ in range(fRs)]
    for ri in range(fRs):
        for ci in range(sCs):
            for index in range(fCs):
                arr[ri][ci] += first[ri][index] * second[index][ci]
    return arr

result = matrix_multiply(
    [[1, 2, 3], [4, 5, 6]],
    [[1, 4], [2, 5], [3, 6]]
)
print(result)
