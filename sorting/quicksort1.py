# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def partition(arr, s):
    smaller = []
    bigger = []
    value = arr[0]
    for x in range(1, s):
        if arr[x] >= value:
            bigger.append(arr[x])
        else:
            smaller.append(arr[x])
    result = smaller + [value] + bigger
    result = [str(i) for i in result]
    print(" ".join(result))


if __name__ == '__main__':
#     size = int(sys.stdin.readline().strip())
#     array = sys.stdin.readline().strip().split()
#     array = [int(i) for i in array]
#     quick_sort(array, size)
    array = [4, 5, 3, 7, 2]
    partition(array, len(array))
