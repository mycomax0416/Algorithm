import copy, sys
sys.stdin = open('17143_BOJ_input.txt', 'r')
from pprint import pprint


def catch(x):
    global size_sum

    for y in range(R):
        if arr[y][x] != 0:
            size_sum += arr[y][x][2]
            arr[y][x] = 0
            return


def move(x, y, s, d, z):
    # if d == 1 or d == 2:
    #     k = s
    #     # k = s % (2*(C-1))

    #     if d == 1:      # 위
    #         if k <= (y+1):
    #             after_arr[y-k][x] = (s, 1, z)
    #         elif (y+1) < k <= (y+1)+R:
    #             after_arr[k-y][x] = (s, 2 ,z)
    #         else:
    #             after_arr[R-(k-(y+1)-R)][x] = (s, 1, z)

    #     elif d == 2:    # 아래
    #         if k <= (R-(y+1):
    #             after_arr[y+k][x] = (s, 2, z)
    #         elif (R-(y+1) < k <= (R-(y+1)+R):
    #             after_arr[R-(k-(R-(y+1)))][x] = (s, 1, z)
    #         else:
    #             after_arr[k-(R-(y+1))-R][x] = (s, 2, z)

    if d == 3 or d == 4:
        k = s
        # k = s % (2*(R-1))

        if d == 3:    # 오른쪽
            if k <= C-(x+1):
                after_arr[y][x+k] = (s, 3, z)
            elif (C-(x+1)) < k <= (C-(x+1))+C:
                after_arr[y][C-(k-(C-(x+1)))] = (s, 4, z)
            else:
                after_arr[y][k-(C-(x+1))-C] = (s, 3, z)
        
        elif d == 4:      # 왼쪽
            if k <= (x+1):
                after_arr[y][x-k] = (s, 4, z)
                # print('a')
            elif (x+1) < k <= (x+1)+C:
                after_arr[y][k-x] = (s, 3 ,z)
                # print('b')
            else:
                after_arr[y][C-(k-(x+1)-C-1))] = (s, 4, z)
                # print('c')

T = int(input())
for t in range(1):
    R, C, M = map(int, input().split())

    arr = [[0]*(C) for _ in range(R)]
    empty_arr = copy.deepcopy(arr)

    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        arr[r-1][c-1] = (s, d, z)
    # pprint(arr)
    size_sum = 0
    # after_arr = copy.deepcopy(empty_arr)
    # move(4, 0, 8, 4, 3)
    # pprint(after_arr)
    for idx in range(C):
        pprint(arr)
        print('------')
        catch(idx)
        pprint(arr)
        print('------')
        after_arr = copy.deepcopy(empty_arr)

        for y in range(R):
            for x in range(C):
                if arr[y][x] != 0:
                    s, d, z = arr[y][x]
                    move(x, y, s, d, z)

        arr = copy.deepcopy(after_arr)
        pprint(arr)
        print('======')
    print(size_sum)