# catalan number used to find num of pairs like:
# # how many pair can we make of 3 * ()
# # answer is: 5 ((())), ()(()), ()()(), (())(), (()())
# catalan number formula is: sum of catalan(i) * catalan(n-i-1)

from time import perf_counter_ns

def catalan_original(n):
    # base case
    if n < 2:
        return 1
    
    res = 0
    for i in range(n):
        res += catalan_original(i) * catalan_original(n-i-1)
    return res

def catalan_mem(n, lookup = {}):
    ''' Using memoization way
    '''
    if n < 2:
        return 1

    if lookup.get(n) is None:
        lookup[n] = 0
        for i in range(0, n):
            lookup[n] += catalan_mem(i, lookup) * catalan_mem(n-i-1, lookup)

    return lookup.get(n)

def catalan_tab(n):   
    ''' Using tabulation way
    '''
    catalan = [0] * (n+1)
    catalan[0] = 1
    catalan[1] = 1

    for i in range(2, n+1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[max(0, i-j-1)]

    return catalan[n]

if __name__ == "__main__":
    # intermediate performance; highest space
    start = perf_counter_ns()
    print(catalan_tab(8))
    end = perf_counter_ns()
    print(end - start)
    # highest performance; intermediate space
    start = perf_counter_ns()
    print(catalan_mem(8))
    end = perf_counter_ns()
    print(end - start)
    # lowest performance; lowest space
    start = perf_counter_ns()
    print(catalan_original(8))
    end = perf_counter_ns()
    print(end - start)