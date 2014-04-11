# -*- coding: utf-8 -*-
# !/usr/bin/python3

import sys


def insert(arr, s):
    value = arr[-1]
    x = -2
    while (x * -1 <= s) and (arr[x] > value):
        arr[x + 1] = arr[x]
        print(" ".join([str(i) for i in arr]))
        x -= 1
    arr[x+1] = value
    print(" ".join([str(i) for i in arr]))

if __name__ == '__main__':
#     size = int(sys.stdin.readline().strip())
#     array = sys.stdin.readline().strip().split()
#     array = [int(x) for x in array]
    array = [2, 4, 6, 8, 1]
    insert(array, 5)
