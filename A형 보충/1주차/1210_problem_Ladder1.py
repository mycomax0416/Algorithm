import sys
sys.stdin = open('1210_sample_input.txt', 'r')

#   동 서 북
dx = [1, -1, 0]
dy = [0, 0, -1]

def DFS(start_x, start_y):
    stack = []
    stack.append((start_x, start_y))
    visit[start_y][start_x] = True

    while stack:
        x, y = stack[-1]
        pre_x, pre_y = x, y

        if y == 0:
            print(x)
            return

        for d in range(3):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < 100 and 0 <= ny < 100 and visit[ny][nx] == False and arr[ny][nx] == 1:
                stack.append((nx, ny))
                visit[ny][nx] = True
                x, y = nx, ny
                break

        if pre_x == x and pre_y == y:
            x, y = stack.pop()
                

for t in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    visit = [[False] * 100 for _ in range(100)]

    for x in range(100):
        if arr[99][x] == 2:
            start = x

    print('#{}'.format(t+1), end=' ')
    DFS(start, 99)