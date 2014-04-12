# -*- coding: utf-8 -*-
# !/usr/bin/python3

import sys


def insertion_sort(arr, s):
    countr = 0
    for v in range(1, len(array)):
        value = arr[v]
        x = v - 1
        while (x >= 0) and (arr[x] > value):
            arr[x + 1] = arr[x]
            x -= 1
            countr += 1
        arr[x+1] = value
    print(" ".join([str(i) for i in arr]))
    print(countr)

if __name__ == '__main__':
#     size = int(sys.stdin.readline().strip())
#     array = sys.stdin.readline().strip().split()
#     array = [int(x) for x in array]
#     insertion_sort(array, size)
    array = [2, 1, 3, 1, 2]
    insertion_sort(array, len(array))
    array = [1, 1, 2, 2, 3, 3, 5, 5, 7, 7, 9, 9]
    insertion_sort(array, len(array))
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    insertion_sort(array, len(array))
