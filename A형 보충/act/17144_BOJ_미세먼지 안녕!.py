import sys, copy
sys.stdin = open('17144_BOJ_input.txt', 'r')


# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def diffusion(x, y, amount):
    div_amount = amount // 5

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < C and 0 <= ny < R and arr[ny][nx] != -1:
            new_arr[ny][nx] += div_amount
            amount -= div_amount

    new_arr[y][x] += amount


def cycle_top():
    for y in range(aircleaner_top-1, 0, -1):
        arr[y][0] = arr[y-1][0]

    arr[0] = arr[0][1::]
    arr[0].append(arr[1][C-1])

    for y in range(1, aircleaner_top):
        arr[y][C-1] = arr[y+1][C-1]

    arr[aircleaner_top] = arr[aircleaner_top][1:C-1]
    arr[aircleaner_top].insert(0, 0)
    arr[aircleaner_top].insert(0, -1)


def cycle_bottom():
    for y in range(aircleaner_bottom+1, R-1):
        arr[y][0] = arr[y+1][0]

    arr[R-1] = arr[R-1][1::]
    arr[R-1].append(arr[R-2][C-1])

    for y in range(R-2, aircleaner_bottom, -1):
        arr[y][C-1] = arr[y-1][C-1]

    arr[aircleaner_bottom] = arr[aircleaner_bottom][1:C-1]
    arr[aircleaner_bottom].insert(0, 0)
    arr[aircleaner_bottom].insert(0, -1)


R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
empty_arr = [[0] * C for _ in range(R)]

for y in range(R):
    if arr[y][0] == -1:
        aircleaner_top = y
        aircleaner_bottom = y+1
        empty_arr[y][0] = -1
        empty_arr[y+1][0] = -1
        break

for t in range(T):
    dusts = []

    for y in range(R):
        for x in range(C):
            if arr[y][x] > 0:
                dusts.append([x, y, arr[y][x]])

    new_arr = copy.deepcopy(empty_arr)

    for dust in dusts:
        diffusion(dust[0], dust[1], dust[2])

    arr = new_arr
    cycle_top()
    cycle_bottom()

result = 0
for y in range(R):
    for x in range(C):
        if arr[y][x] > 0:
            result += arr[y][x]

print(result)