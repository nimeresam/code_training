def cutRod(price, n):
    if n <= 0:
        return 0

    max_val = 0
    for index in range(n):
        max_val = max(max_val, price[index] + cutRod(price, n - index - 1))
    return max_val

def cutRodMemo(price, n, memo):
    if n <= 0:
        return 0
    
    max_val = 0
    for index in range(n):
        required = n - index - 1 
        prev = memo.get(required, None)
        if not prev:
            prev = cutRodMem(price, required, memo)
            memo[required] = prev
        max_val = max(max_val, price[index] + prev)
    return max_val


# Driver code 
arr = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30] 
size = len(arr) 
best_val = cutRodMem(arr, 10, {})
print("Maximum Obtainable Value is", best_val) 