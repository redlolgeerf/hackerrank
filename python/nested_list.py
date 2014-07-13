# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import sys

if __name__ == '__main__':
    students = []
    number_of_students = int(sys.stdin.readline().strip())
    for x in range(number_of_students):
        name = sys.stdin.readline().strip()
        mark = float(sys.stdin.readline().strip())
        students.append([mark, name])
    
    students.sort()
    mark_min = students[0][0]
    second_min = students[-1][0]
    for student in students:
        if student[0] > mark_min:
            if student[0] <= second_min:
                second_min = student[0]
                print(student[1])
            else:
                break


