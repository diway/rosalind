# fib numbers

# Complex O(2^n)
def fib1(n):
    if (n == 0): return 0
    if (n == 1): return 1
    return fib1(n-2) + fib1(n-1)

# Complex O(n)
fib_nums = [None] * 26
def fib2(n):
    if (n == 0): return 0
    if (n == 1): return 1
    if (fib_nums[n]): return fib_nums[n]
    fib_nums[n] = fib2(n-2) + fib2(n-1)
    return fib_nums[n]

# Complex O(n)
def fib3(n):
    if (n == 0): return 0
    a, b = 0, 1
    while n-1:
        a, b = b, a+b
        n -= 1 
    return b

# Complex O(log(n))
def fib4(n):
    # matrix a = |1 1|
    #            |1 0|
    a = [1, 1, 1, 0]
    # matrix r = |f(n)  |, initial |f(1)|
    #            |f(n-1)|          |f(0)|
    # a * r = |f(n+1)|
    #         |f(n)  |
    r = [1, 0]
    while n:
        if (n & 1 == 1):
            # r = a * r
            r = [a[0]*r[0] + a[1]*r[1], a[2]*r[0] + a[3]*r[1]]
        # a = a * a
        a = [a[0]**2   + a[1]*a[2], a[0]*a[1] + a[1]*a[3],
             a[0]*a[2] + a[2]*a[3], a[1]*a[2] + a[3]**2]
        n >>= 1
    return r[1]

print fib4(10)