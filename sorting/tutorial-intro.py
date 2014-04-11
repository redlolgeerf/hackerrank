# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def index(value, size, array):
    return array.index(value)

if __name__ == '__main__':
    v = sys.stdin.readline().strip()
    n = sys.stdin.readline().strip()
    ar = sys.stdin.readline().strip().split()
    print(index(v, n, ar))
