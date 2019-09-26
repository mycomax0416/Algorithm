import sys, copy
sys.stdin = open('input_3.txt', 'r')


def robot_position():
    for y in range(M):
        for x in range(N):
            if arr[y][x] == 1:
                return x, y


def work(robot_x, robot_y, c, m, last_m):
    global max_m

    if c == 0:
        max_m = max(max_m, m)
        return

    elif c < 0:
        max_m = max(max_m, m-last_m)
        return

    # if max_m != 0:
    #     if m < max_m/C*(C-c):
    #         return

    elif c <= C*3/4 and m <= max_m*1/4:
        return

    elif c <= C/2 and m <= max_m/2:
        return

    elif c <= C/4 and m <= max_m*3/4:
        return

    else:
        tests = []
        for y in range(M):
            for x in range(N):
                if arr[y][x] != 0 and arr[y][x] != 1:
                    tests.append((x, y))

        for test in tests:
            t_x, t_y = test
            befo = arr[t_y][t_x]
            arr[t_y][t_x] = 0

            work(robot_x, robot_y, c-2*(abs(robot_x-t_x)+abs(robot_y-t_y)), m+befo, befo)

            arr[t_y][t_x] = befo


T = int(input())
for t in range(T):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_m = 0
    x, y = robot_position()

    work(x, y, C, 0, 0)

    print('#{} {}'.format(t+1, max_m))
