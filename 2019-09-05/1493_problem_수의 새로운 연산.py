import sys
sys.stdin = open('1493_sample_input.txt', 'r')


def func_sharp(x, y):
    cal = 0
    for val in range(1, x+y):
        cal += val

    cal -= y

    return cal + 1


def func_and(num):
    cal = 0
    line = 0
    for val in range(1, 20001):
        pre = cal + val
        line += 1
        if cal < num <= pre:
            break

        else:
            cal = pre

    for y in range(0, pre):
        if pre - y == num:
            return line-y, y+1


def func_plus(point_1, point_2):
    return point_1[0]+point_2[0], point_1[1]+point_2[1]


def func_star(p, q):
    x, y = func_plus(func_and(p), func_and(q))
    return func_sharp(x, y)


T = int(input())
for t in range(T):
    p, q = map(int, input().split())
    
    print('#{} {}'.format(t+1, func_star(p, q)))
