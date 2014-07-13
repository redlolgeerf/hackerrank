# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def fib(limit):
    a, b = 0, 0
    while limit > 0:
        limit -= 1
        yield a+b
        a, b = b, a+b
        if a == 0 and b == 0:
            a = 1

if __name__ == '__main__':
    limit = int(sys.stdin.readline().strip())
    print(list(map(lambda x: x**3, [i for i in fib(limit)])))
