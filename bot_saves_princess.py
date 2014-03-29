#!/usr/bin/python3
import sys


def displayPathtoPrincess(n, grid):
    import sys

    bot_y, bot_x = None, None
    princess_y, princess_x = None, None

    y = 0
    for line in grid:
        x = 0
        if (bot_y is not None) and (bot_x is not None) and (princess_y is not None) and (princess_x is not None):
            break

        for square in line:
            if square == 'm':
                bot_y, bot_x = y, x
            elif square == 'p':
                princess_y, princess_x = y, x
            x += 1

        y += 1
    # print('y is %d, x is %d' % (bot_y, bot_x))
    # print('y is %d, x is %d' % (princess_y, princess_x))
    while bot_x != princess_x:
        if bot_x < princess_x:
            sys.stdout.write('RIGHT\n')
            bot_x += 1
        elif bot_x > princess_x:
            sys.stdout.write('LEFT\n')
            bot_x -= 1

    while bot_y != princess_y:
        if bot_y < princess_y:
            sys.stdout.write('DOWN\n')
            bot_y += 1
        elif bot_y > princess_y:
            sys.stdout.write('UP\n')
            bot_y -= 1

#print all the moves here
m = int(sys.stdin.readline())
grid = []
for i in range(0, m):
    grid.append(sys.stdin.readline().strip())

displayPathtoPrincess(m, grid)


