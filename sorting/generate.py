# !/usr/bin/python3
# -*- coding: utf-8 -*-

import random

res = []

for x in range(30000):
    res.append(random.randint(0, 10**9))

print(" ".join([str(i) for i in res]))
