import random
import sys


def random_square():
    return int(random.random() * (field_size))


def make_field(field_size, target_ammount):
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
                square = 'd'
            field += square

    field = str(field_size) + '\n' + str(r) + ' ' + str(c) + field
    return field

if __name__ == '__main__':
    print('Please enter the field size')
    field_size = int(sys.stdin.readline())
    print('Please enter the amount of targets')
    target_ammount = int(sys.stdin.readline())
    print(make_field(field_size, target_ammount))
else:
    field_size = int(random.random() * 100)
    target_ammount = int(random.random() * field_size / 2)
