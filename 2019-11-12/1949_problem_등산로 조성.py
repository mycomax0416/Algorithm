import sys
sys.stdin = open('1949_sample_input.txt', 'r')
from collections import deque


def find_height():
    global max_height

    for y in range(N):
        for x in range(N):
            max_height = max(max_height, arr[y][x])


# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def go(start_x, start_y):
    global max_distance

    Q = deque()
    Q.append((start_x, start_y, 1))

    while Q:
        x, y, distance = Q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and arr[y][x] > arr[ny][nx]:
                Q.append((nx, ny, distance+1))
                max_distance = max(max_distance, distance+1)


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_distance = 0

    max_height = 0
    find_height()

    starts = []
    for y in range(N):
        for x in range(N):
            if arr[y][x] == max_height:
                starts.append((x, y))


    for y in range(N):
        for x in range(N):
            for k in range(K):
                before_value = arr[y][x]
                arr[y][x] -= k+1

                for test_x, test_y in starts:
                    go(test_x, test_y)

                arr[y][x] = before_value

    print('#{} {}'.format(t+1, max_distance))