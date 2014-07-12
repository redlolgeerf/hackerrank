# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import sys

if __name__ == '__main__':
    students = {}
    student_number = int(sys.stdin.readline().strip())
    for student in range(student_number):
        student_name, *marks = sys.stdin.readline().strip().split()
        students[student_name] = [float(x) for x in marks]

    question = sys.stdin.readline().strip()
    marks = students[question]
    x = sum(marks) / len(marks)
    sys.stdout.write(format(x, '0.2f'))

