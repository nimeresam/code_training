def cutRod(price, n):
    if n <= 0:
        return 0

    max_val = 0
    for index in range(n):
        max_val = max(max_val, price[index] + cutRod(price, n - index - 1))
    return max_val


# Driver code 
arr = [1, 8, 5] 
size = len(arr) 
print("Maximum Obtainable Value is", cutRod(arr, size)) 