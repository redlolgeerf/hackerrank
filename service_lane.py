import sys


def compose(n, f, t=0):
    s = 3 * f + 5 * t
    if s == n:
        return '5' * 3 * f + '3' * 5 * t
    if n < 3:
        return -1
    if s < n:
        return compose(n, f, t + 1)
    if f > 0 and s > n:
        return compose(n, f - 1, t)
    if f == 0 and s > n:
        return -1
    else:
        return -1

test_count = int(sys.stdin.readline())
# tests = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in range(test_count):
    test_case = int(sys.stdin.readline())
    sys.stdout.write(str(compose(test_case, test_case // 3)) + '\n')

# for test in tests:
#     # try:
#     print(compose(test, test // 3))
#     # except:
    #     print(test)