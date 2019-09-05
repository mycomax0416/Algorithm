import sys
sys.stdin = open('15683_BOJ_input.txt', 'r')

camera = [1, 2, 3, 4, 5]
#       동 서 남 북
dx_1 = [1, -1, 0, 0]
dy_1 = [0, 0, 1, -1]


def camara_1(x, y, d):
    global N, M

    # for d in range(4):
    nx = x + dx_1[d]
    ny = y + dy_1[d]
    while 0 <= nx < M and 0 <= ny < N and arr[ny][nx] != 6:
        if arr[ny][nx] in camera:
            nx += dx_1[d]
            ny += dy_1[d]

        else:
            arr[ny][nx] = '#'
            nx += dx_1[d]
            ny += dy_1[d]
    return


def find():
    for y in range(N):
        for x in range(M):
            if arr[y][x] in camera:
                cameras.append([x, y, arr[y][x]])
    return


T = int(input())
for t in range(1):
    N, M = map(int, input().split())    # N : 세로, M : 가로
    # print(N, M)

    cameras = []

    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)

    find()
    print(cameras)
    camara_1(2, 2, 1)
    print(arr)


