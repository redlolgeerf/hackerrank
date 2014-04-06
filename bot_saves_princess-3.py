import sys

def get_coordinates(n, grid, target, target_ammount=None):
    if target_ammount is None:
        target_ammount = n**n
    targets = []

    y = 0
    for line in grid:
        x = 0
        if len(targets)==target_ammount:
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

def move(bot_x, bot_y, target_x, target_y):
    cleaned = False
    if bot_x < target_x:
        print('RIGHT')
        bot_x += 1
    elif bot_x > target_x:
        print('LEFT')
        bot_x -= 1
    elif bot_y < target_y:
        print('DOWN')
        bot_y += 1
    elif bot_y > target_y:
        print('UP')
        bot_y -= 1
    elif (bot_x == target_x and
         bot_y == target_y):
        print('CLEAN')
        cleaned = True
    else:
        raise Error
    return (bot_x, bot_y, cleaned)

n = int(sys.stdin.readline())
r, c = [int(i) for i in sys.stdin.readline().strip().split()]
grid = []

for i in range(0, n):
    grid.append(sys.stdin.readline())

targets = get_coordinates(n, grid, 'p')
targets = get_distance(targets, r, c)

while targets:
    target = min(targets, key=lambda x: x[2]) # FIXME sort by third element - target[2]
    targets.remove(target)
    cleaned = False
    while not cleaned:
        r, c, cleaned = move(r, c, target[0], target[1])

