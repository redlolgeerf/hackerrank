# -*- coding: utf-8 -*-
# !/usr/bin/python3

import sys


def insert(arr, s, v):
    value = arr[v]
    x = v - 1
    while (x >= 0) and (arr[x] > value):
        arr[x + 1] = arr[x]
        x -= 1
    arr[x+1] = value
    print(" ".join([str(i) for i in arr]))

if __name__ == '__main__':
    size = int(sys.stdin.readline().strip())
    array = sys.stdin.readline().strip().split()
    array = [int(x) for x in array]
#     array = [1, 4, 3, 5, 6, 2]
    for value in range(1, len(array)):
        insert(array, size, value)
