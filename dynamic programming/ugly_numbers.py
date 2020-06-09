from time import perf_counter_ns

def get_nth_ugly_no(n):

    def max_divide(a, b):
        while a % b == 0:
            a = a / b
        return a

    def is_ugly(no):
        no = max_divide(no, 2)
        no = max_divide(no, 3)
        no = max_divide(no, 5)
        return no == 1

    no = 1
    i = 1
    while i < n:
        no += 1
        if is_ugly(no):
            i += 1
    return no

def get_nth_ugly_no_dynamic(n):
    ugly = [0] * n
    ugly[0] = 1

    i2 = i3 = i5 = 0

    for i in range(1, n):
        next_i2 = ugly[i2] * 2
        next_i3 = ugly[i3] * 3
        next_i5 = ugly[i5] * 5

        ugly[i] = min(next_i2, next_i3, next_i5)

        if next_i2 == ugly[i]:
            i2 += 1

        if next_i3 == ugly[i]:
            i3 += 1 

        if next_i5 == ugly[i]:
            i5 += 1
    
    return ugly[-1]


if __name__ == "__main__":
    # highest performance; highest space
    start = perf_counter_ns()
    print(get_nth_ugly_no_dynamic(150))
    end = perf_counter_ns()
    print(end - start)
    # lowest performance; lowest space
    start = perf_counter_ns()
    print(get_nth_ugly_no(150))
    end = perf_counter_ns()
    print(end - start)
        