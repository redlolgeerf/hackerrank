import random
import sys


def random_square():
    return int(random.random() * (field_size))

field_size = int(sys.stdin.readline())
target_ammount = int(sys.stdin.readline())

targets = set([(random_square(), random_square())
               for x in range(target_ammount)])

r, c = (random_square(), random_square())

field = ''

for y in range(field_size):
    for x in range(field_size):
        if x == 0:
            field += '\n'
        square = '-'
        if (x, y) == (r, c):
            square = 'b'
        if (x, y) in targets:
            square = 'p'
        field += square

field = str(field_size) + '\n' + str(r) + ' ' + str(c) + field
print(field)
