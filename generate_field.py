import random
import sys


def random_square(n):
    return int(random.random() * (n))


def gen_coordinates(field_size, target_ammount):
    targets = set([(random_square(field_size), random_square(field_size))
                  for x in range(target_ammount)])

    r, c = (random_square(field_size), random_square(field_size))

    return r, c, targets


def make_field(field_size=None, bot_x=None, bot_y=None, target_ammount=None):
    if field_size is None or target_ammount is None:
        field_size = int(random.random() * 10)
        target_ammount = int(random.random() * field_size / 2)

    r, c, targets = gen_coordinates(field_size, target_ammount)

    if (bot_x is not None) and (bot_y is not None):
        r, c = bot_x, bot_y

    return draw_field(field_size, r, c, targets)


def draw_field(field_size, r, c, targets):
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
    print('')
    print(make_field(field_size=field_size, target_ammount=target_ammount))
