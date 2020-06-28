class area:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def getMaxSurvivalTime(a, b, x, y, z):
    if a <= 0 or b <= 0:
        return 0
    memo = dict()

    return max(
        maxSurvival(a + x.a, b + x.b, x, y, z, 1, memo),
        maxSurvival(a + y.a, b + y.b, x, y, z, 2, memo),
        maxSurvival(a + z.a, b + z.b, x, y, z, 3, memo)
    )

def maxSurvival(a, b, x, y, z, last, memo):
    if a <= 0 or b <= 0:
        return 0

    cur = area(a, b)
    # check if already calculated 
    for ar in memo.keys():
        if ar.a == a and ar.b == b:
            return memo[ar]

    if last == 1:
        temp = 1 + max(
            maxSurvival(a + y.a, b + y.b, x, y, z, 2, memo),
            maxSurvival(a + z.a, b + z.b, x, y, z, 3, memo)
        )
    elif last == 2:
        temp = 1 + max(
            maxSurvival(a + x.a, b + x.b, x, y, z, 1, memo),
            maxSurvival(a + z.a, b + z.b, x, y, z, 3, memo)
        )
    elif last == 3:
        temp = 1 + max(
            maxSurvival(a + x.a, b + x.b, x, y, z, 1, memo),
            maxSurvival(a + y.a, b + y.b, x, y, z, 2, memo)
        )

    memo[cur] = temp
    return temp

X = area(3, 2) 
Y = area(-5, -10) 
Z = area(-20, 5) 
  
A = 20
B = 8
print(getMaxSurvivalTime(A, B, X, Y, Z)) 