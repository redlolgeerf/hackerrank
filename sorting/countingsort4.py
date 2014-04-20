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
        array.append(sys.stdin.readline().strip())

    array = [i.split() for i in array]
    numbers = [int(i[0]) for i in array]

    arr = counting(numbers, size)

    counter = 0
    sorted_arr = []

    for x in range(100):
        counter += arr[x]
        sorted_arr.append(counter)

    result = []
    help_arr = []

    for x in array:
        result.append('')

    for x in range(100):
        help_arr.append(0)

    for x in range(size):
        if int(array[x][0]) == 0:
            place = 0
        else:
            place = sorted_arr[int(array[x][0]) - 1]

        i = help_arr[int(array[x][0])]

        if x < (size // 2):
            result[place + i] = '-'
        else:
            result[place + i] = array[x][1]

        help_arr[int(array[x][0])] += 1

    print(" ".join(result))
