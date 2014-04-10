import sys


def get_coordinates(n, grid, target, target_ammount=None):
    if target_ammount is None:
        target_ammount = n**n
    targets = []

    y = 0
    for line in grid:
        x = 0
        if len(targets) == target_ammount:
            break
        for square in line:
            if square == target:
                targets.append([x, y])
            x += 1
        y += 1
    return targets


def get_distance(targets, bot_x, bot_y):
    distances = []
    for target in targets:
        distance = abs(target[0] - bot_x) + abs(target[1] - bot_y)
        distances.append([target[0], target[1], distance])
    return distances


def single_move(bot_x, bot_y, target_x, target_y):
    cleaned = False
    if bot_x < target_x:
        move = 'RIGHT'
        bot_x += 1
    elif bot_x > target_x:
        move = 'LEFT'
        bot_x -= 1
    elif bot_y < target_y:
        move = 'DOWN'
        bot_y += 1
    elif bot_y > target_y:
        move = 'UP'
        bot_y -= 1
    elif (bot_x == target_x and
          bot_y == target_y):
        move = 'CLEAN'
        cleaned = True
    return (bot_x, bot_y, cleaned, move)


def parse_grid(field):
    if field is None:
        n = int(sys.stdin.readline())
        r, c = [int(i) for i in sys.stdin.readline().strip().split()]
        grid = []

        for i in range(0, n):
            grid.append(sys.stdin.readline())
    else:
        n = int(field[0])
        r, c = int(field[1].split()[0]), int(field[1].split()[1])
        grid = field[2:]
    return n, r, c, grid


def moves(field=None, target='p'):
    n, r, c, grid = parse_grid(field)
    targets = get_coordinates(n, grid, target)

    moves = []
    while targets:
        distances = get_distance(targets, r, c)
        target = min(distances, key=lambda x: x[2])
        targets.remove(target[:2])
        cleaned = False
        while not cleaned:
            r, c, cleaned, move = single_move(r, c, target[0], target[1])
            moves.append(move)
    return moves


def next_move(posr, posc, board):
    n = 5
    r, c = posc, posr

    targets = get_coordinates(n, board, 'd')

    distances = get_distance(targets, r, c)
    target = min(distances, key=lambda x: x[2])
    r, c, cleaned, move = single_move(r, c, target[0], target[1])
    print(move)

if __name__ == '__main__':
    moves = moves()
    for move in moves:
        print(move)
