import sys

def memo(f):
    cache = {}
    def wrapper(a):
        if a not in cache:
            cache[a] = f(a)
        return cache[a]
    return wrapper

@memo
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def if_fibo(s):
    a = 0
    while s >= fib(a):
        if s == fib(a):
            sys.stdout.write('IsFibo\n')
            return
        a += 1
    sys.stdout.write('IsNotFibo\n')

test_count = int(sys.stdin.readline())

for i in range(test_count):
    test_case = int(sys.stdin.readline())
    if_fibo(test_case)
