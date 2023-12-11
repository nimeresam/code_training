def isSubsetSum(set, n, sum):
    # Base Case
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

    # if the last element is greater than sum
    # just ignore it
    if set[n-1] > sum:
        return isSubsetSum(set, n-1, sum)

    return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1])

def isSubsetSum_tabulation(set, n, sum):
    # create 2D array of sum + 1 * n + 1
    # fill first column with True
    # fill first row with False
    # default value is False
    subset = [[col == 0 for col in range(sum + 1)] for row in range(n+1)]

    # since first col is True
    # and first row is False
    # will start from second row and second column
    for row in range(1, n+1):
        # find element that we should compare with
        element = set[row-1]
        for col in range(1, sum+1):
            if col < element:
                subset[row][col] = subset[row-1][col]
            else:
                subset[row][col] = subset[row-1][col] or subset[row-1][col-element]

# Driver program to test above function 
if __name__=='__main__': 
    set = [3, 34, 4, 12, 5, 2] 
    sum = 9
    n = len(set) 
    if (isSubsetSum(set, n, sum) == True): 
        print("Found a subset with given sum") 
    else: 
        print("No subset with given sum") 