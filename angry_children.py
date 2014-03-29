import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

n_list = []

for i in range(n):
    n_list.append(int(sys.stdin.readline()))

n_list.sort()

minim = n_list[-1]

for i in range(n - k):
    s = n_list[i + k - 1] - n_list[i]
    if s < minim:
        minim = s

sys.stdout.write(str(minim))
