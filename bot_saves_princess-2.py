import sys


def nextMove(n, r, c, grid):
    bot_y, bot_x = r, c
    princess_y, princess_x = None, None

    y = 0
    for line in grid:
        x = 0
        if (princess_y is not None) and (princess_x is not None):
            break

        for square in line:
            if square == 'p':
                princess_y, princess_x = y, x
            x += 1

        y += 1

    if bot_x < princess_x:
        move = 'RIGHT'
    elif bot_x > princess_x:
        move = 'LEFT'
    elif bot_y < princess_y:
        move = 'DOWN'
    elif bot_y > princess_y:
        move = 'UP'
    else:
        move = None
    return move if move is not None else 1

n = int(sys.stdin.readline())
r, c = [int(i) for i in sys.stdin.readline().strip().split()]
grid = []

for i in range(0, n):
    grid.append(sys.stdin.readline())

print(nextMove(n, r, c, grid))
