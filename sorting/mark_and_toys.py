# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import time


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
    return result


if __name__ == '__main__':
    size, k = sys.stdin.readline().strip().split()
    size, k = int(size), int(k)

    array_a = sys.stdin.readline().strip().split()
    array_a = [int(i) for i in array_a]

    example = sorted(array_a)

    array_a = partition(array_a, len(array_a))

    total = 0
    counter = 0
    for i, value in enumerate(array_a):
        if total + value <= k:
            total += value
            counter = i + 1
        else:
            break
    print(counter)
