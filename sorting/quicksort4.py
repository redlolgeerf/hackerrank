# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


quick_counter = 1
insert_counter = 0

def partition(arr, s):
    global quick_counter
    if s == 1:
        quick_counter += 1
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
    quick_counter += 1
    result = partition(smaller, len(smaller)) + [value] + \
             partition(bigger, len(bigger))
    return result


def insertion_sort(arr, s):
    global insert_counter
    for v in range(1, len(array)):
        value = arr[v]
        x = v - 1
        while (x >= 0) and (arr[x] > value):
            arr[x + 1] = arr[x]
            x -= 1
            insert_counter += 1
        arr[x+1] = value
    return arr


if __name__ == '__main__':
#     size = int(sys.stdin.readline().strip())
#     array = sys.stdin.readline().strip().split()
#     array = [int(i) for i in array]
    array = [1, 3, 9, 8, 2, 7, 5]
#    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#     print("Quick sort")
#     print(" ".join([str(i) for i in partition(array, len(array))]))
#     print(quick_counter)
#     print("Insert sort")
#     print(" ".join([str(i) for i in insertion_sort(array, len(array))]))
#     print(insert_counter)
    size = len(array)
    insertion_sort(array, size)
    partition(array, size)
    print(insert_counter - quick_counter)
