import sys
sys.stdin = open('1405_BOJ_input.txt', 'r')


# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def move(x, y, k, p):
    global result

    if k >= count:
        result += p
        return

    else:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < 29 and 0 <= ny < 29 and visit[ny][nx] == False:
                visit[ny][nx] = True

                move(nx, ny, k+1, p*options[d]/100)

                visit[ny][nx] = False
                 

count, E, W, S, N = map(int, input().split())
options = [E, W, S, N]

visit = [[False] * 29 for _ in range(29)]
start_x, start_y = 14, 14
visit[start_y][start_x] = True

result = 0

move(start_x, start_y, 0, 100)

print(result/100)
