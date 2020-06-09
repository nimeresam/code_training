def count_original(cl, cc, amount):
    '''
    Arguments:
        cl {number[]} -- coins list
        cc {number} -- coins count
        amount {number} -- amount to be changed
    '''

    if amount == 0:
        return 1

    if amount < 0:
        return 0

    if cc <= 0:
        return 0

    return count_original(cl, cc-1, amount) + count_original(cl, cc, amount - cl[cc-1])
    
if __name__ == "__main__":
    print(count_original([5, 10, 25, 50], 4, 100))