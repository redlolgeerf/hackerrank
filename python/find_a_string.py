# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import sys

def find_occurences(a, b):
    occurences = 0
    for i in range(len(a)):
        if a[i:].startswith(b):
            occurences += 1
    return occurences

if __name__ == '__main__':
    string = sys.stdin.readline().strip()
    search_string = sys.stdin.readline().strip()
    sys.stdout.write(format(find_occurences(string, search_string), ''))
