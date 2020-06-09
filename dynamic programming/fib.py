from time import perf_counter_ns

def fib_original(n):
    # Base Case
    if n < 2:
        return n

    return fib_original(n-1) + fib_original(n-2)


def fib_mem(n, lookup={}):
    ''' Using memoization way
    '''
    # Base Case
    if n == 0 or n == 1:
        lookup[n] = n

    if lookup.get(n) is None:
        lookup[n] = fib_mem(n-1, lookup) + fib_mem(n-2, lookup)

    return lookup[n]

def fib_tab(n):
    ''' Using tabulation way
    '''
    f = [0] * (n+1)
    f[1] = 1

    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

if __name__ == "__main__":
    # highest performance; highest space
    start = perf_counter_ns()
    print(fib_tab(34))
    end = perf_counter_ns()
    print(end - start)
    # intermediate performance; intermediate space
    start = perf_counter_ns()
    print(fib_mem(34))
    end = perf_counter_ns()
    print(end - start)
    # lowest performance; lowest space
    start = perf_counter_ns()
    print(fib_original(34))
    end = perf_counter_ns()
    print(end - start)