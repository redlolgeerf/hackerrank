# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def partition(arr, s):
    if s == 1:
        return arr
    if s == 0:
        return []
    smaller = []
    bigger = []
    value = arr[0]
    for x in range(1, s):
        if arr[x] >= value:
            bigger.append(arr[x])
        else:
            smaller.append(arr[x])
    result = partition(smaller, len(smaller)) + [value] + \
             partition(bigger, len(bigger))
    print(" ".join([str(i) for i in result]))
    return result


if __name__ == '__main__':
#     size = int(sys.stdin.readline().strip())
#     array = sys.stdin.readline().strip().split()
#     array = [int(i) for i in array]
#     quick_sort(array, size)
    #array = [4, 5, 3, 7, 2]
    #partition(array, len(array))
    array = [5, 8, 1, 3, 7, 9, 2]
    partition(array, len(array))
