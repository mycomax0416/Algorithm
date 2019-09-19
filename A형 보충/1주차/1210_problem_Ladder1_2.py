import sys
sys.stdin = open('1210_sample_input.txt', 'r')

#   동 서 북
dx = [1, -1, 0]
dy = [0, 0, -1]

def go(start_x, start_y):
    if start_y == 0:
        print(start_x)
        return

    for d in range(3):
        nx = start_x + dx[d]
        ny = start_y + dy[d]

        if 0 <= nx < 100 and 0 <= ny < 100 and visit[ny][nx] == False and arr[ny][nx] == 1:
            visit[ny][nx] = True
            go(nx, ny)
            return


for t in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    visit = [[False] * 100 for _ in range(100)]

    for x in range(100):
        if arr[99][x] == 2:
            start = x

    print('#{}'.format(t+1), end=' ')
    go(start, 99)