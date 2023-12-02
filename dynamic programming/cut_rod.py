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

def cutRodTab(price, n):
    max_profits = [0] * (n+1)
    directions = [0] * (n+1)
    for oi in range(n):
        for ii in range(oi + 1):
            next_val = price[ii] + max_profits[oi - ii]
            if max_profits[oi + 1] < next_val:
                max_profits[oi + 1] = next_val
                directions[oi + 1] = ii + 1
    return max_profits[-1]

# Driver code 
arr = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30] 
size = len(arr) 
best_val = cutRodTab(arr, 10)
print("Maximum Obtainable Value is", best_val) 