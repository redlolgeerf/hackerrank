# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import sys
import xml.etree.ElementTree as etree


def count_score(element):
    score = len(element.attrib)
    if len(element) == 0:
        return score
    return score + sum(count_score(child) for child in element)

if __name__ == '__main__':
    lines_number = int(sys.stdin.readline().strip())
    xml = []
    for line in range(lines_number):
        xml.append(sys.stdin.readline())
    tree = etree.ElementTree(etree.fromstring(" ".join(xml)))
    root = tree.getroot()
    score = count_score(root)
    print(score)
