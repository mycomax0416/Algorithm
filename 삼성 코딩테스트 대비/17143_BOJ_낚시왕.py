import sys, copy
from pprint import pprint
sys.stdin = open('17143_BOJ_input.txt', 'r')


def catch(x):
    global size_sum

    for y in range(C):
        if arr[y][x] != 0:
            size_sum += arr[y][x][0]
            return


T = int(input())
for t in range(1):
    R, C, M = map(int, input().split())

    arr = [[0]*(R) for _ in range(C)]
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        arr[c-1][r-1] = (s, d, z)

    empty_arr = copy.deepcopy(arr)

    pprint(arr)

    for y in range(C):
        for x in range(R):
            if arr[y][x] != 0:
                s, d, z = arr[y][x]
                # print(s, d, z)

    size_sum = 0

    for idx in range(R):
        print(idx)