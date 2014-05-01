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
    return result


if __name__ == '__main__':
    test_cases = int(sys.stdin.readline().strip())
    for test in range(test_cases):
        size, k = sys.stdin.readline().strip().split()
        size, k = int(size), int(k)

        array_a = sys.stdin.readline().strip().split()
        array_a = [int(i) for i in array_a]
        array_b = sys.stdin.readline().strip().split()
        array_b = [int(i) for i in array_b]

        array_a = partition(array_a, size)
        temp = partition(array_b, size)
        array_b = temp[::-1]
#         print(array_a)
#         print(array_b)

        for i in range(size):
            if array_a[i] + array_b[i] < k:
                print('NO')
                break
        else:
            print('YES')
