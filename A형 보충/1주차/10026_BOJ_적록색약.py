import sys, copy
sys.stdin = open('10026_BOJ_input.txt', 'r')


def find():
    global count

    for y in range(N):
        for x in range(N):
            if arr[y][x] != 0:
                count += 1
                return x, y, arr[y][x]


# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def section(start_x, start_y, color):
    stack = []
    visit = [[False] * N for _ in range(N)]

    stack.append((start_x, start_y))
    visit[start_y][start_x] = True
    arr[start_y][start_x] = 0

    while stack:
        x, y = stack[-1][0], stack[-1][1]
        pre_x, pre_y = x, y

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and visit[ny][nx] == False and arr[ny][nx] == color:
                stack.append((nx, ny))
                visit[ny][nx] = True
                arr[ny][nx] = 0
                x, y = nx, ny
                break

        if pre_x == x and pre_y == y:
            stack.pop()


N = int(input())
arr = [list(input()) for _ in range(N)]

arr_error = copy.deepcopy(arr)
for y in range(N):
    for x in range(N):
        if arr_error[y][x] == 'G':
            arr_error[y][x] = 'R'

empty = [[0] * N for _ in range(N)]

count = 0

while arr != empty:
    start_x, start_y, color = find()
    section(start_x, start_y, color)

print(count, end=' ')

arr = arr_error
count = 0

while arr != empty:
    start_x, start_y, color = find()
    section(start_x, start_y, color)

print(count)