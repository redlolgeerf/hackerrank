# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def counting(arr, s):
    appearences = []
    for x in range(100):
        appearences.append(0)
    for value in arr:
        appearences[value] += 1
    return appearences

if __name__ == '__main__':
    size = int(sys.stdin.readline().strip())
    array = []
    for x in range(size):
        array.append(sys.stdin.readline().strip().split()[0])
    array = [int(i) for i in array]

    arr = counting(array, size)
    counter = 0
    result = []
    for x in range(100):
        counter += arr[x]
        result.append(counter)
    print(" ".join(str(i) for i in result))
