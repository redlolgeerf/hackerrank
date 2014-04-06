import random
import sys

field_size = int(sys.stdin.readline())
target_ammount = int(sys.stdin.readline())

targets = set([(int(random.random() * (field_size + 1)), int(random.random() * (field_size + 1 ))) for x in range(target_ammount)])

r, c = ((random.random() * (field_size + 1)), (random.random() * (field_size + 1))
field = str(field_size) + '/n' + str(r) + ' ' + str(c)
print(targets)

