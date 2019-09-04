import sys
sys.stdin = open('6515_sample_input.txt', 'r')

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, -1, 1, 1, -1]

def game(x, y, color):
    global arr
    global N
    x -= 1
    y -= 1

    arr[y][x] = color

    if color == 1:
        opposite = 2
    elif color == 2:
        opposite = 1

    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        sign = False

        while 0 <= nx < N and 0 <= ny < N and arr[ny][nx] == opposite:
            nx += dx[d]
            ny += dy[d]

            if 0 <= nx < N and 0 <= ny < N and arr[ny][nx] == color:
                sign = True
                break

        if sign == True:
            ix, iy = x, y

            if ix > nx:
                ix, nx = nx, ix
            if iy > ny:
                iy, ny = ny, iy

            for ty in range(iy, ny+1):
                for tx in range(ix, nx+1):
                    if d < 4:
                        arr[ty][tx] = color

                    elif 4 <= d < 6:
                        if abs(tx + ty) == x + y:
                            arr[ty][tx] = color
                
                    elif 6 <= d < 8:
                        if abs(tx) == abs(ty):
                            arr[ty][tx] = color

    return

T = int(input())
for t in range(T):
    N, M = map(int, input().split())

    arr = [[0] * N for _ in range(N)]
    arr[N//2][N//2-1] = 1
    arr[N//2-1][N//2] = 1
    arr[N//2-1][N//2-1] = 2
    arr[N//2][N//2] = 2

    for m in range(M):
        x, y, color = map(int, input().split())
        game(x, y, color)

    white = 0
    black = 0

    for y in range(N):
        for x in range(N):
            if arr[y][x] == 1:
                black += 1
            elif arr[y][x] == 2:
                white += 1

    print('#{} {} {}'.format(t+1, black, white))
