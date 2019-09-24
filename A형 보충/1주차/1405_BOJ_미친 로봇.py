import sys
sys.stdin = open('1405_BOJ_input.txt', 'r')


# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def move(k):
    global x, y, result, possibility

    if k >= action:
        result += possibility
        visit[y][x] = False
        return

    else:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < 29 and 0 <= ny < 29 and visit[ny][nx] == False:
                visit[ny][nx] = True
                pre_x, pre_y = x, y
                x, y = nx, ny

                if d == 0:
                    if E != 0:
                        possibility *= E/100
                        move(k+1)
                        possibility /= E/100
                    else:
                        possibility *= 0
                        return
                    
                elif d == 1:
                    if W != 0:
                        possibility *= W/100
                        move(k+1)
                        possibility /= W/100
                    else:
                        possibility *= 0
                        return

                elif d == 2:
                    if S != 0:
                        possibility *= S/100
                        move(k+1)
                        possibility /= S/100
                    else:
                        possibility *= 0
                        return

                else:
                    if N != 0:
                        possibility *= N/100
                        move(k+1)
                        possibility /= N/100
                    else:
                        possibility *= 0
                        return

                visit[ny][nx] = False
                x, y = pre_x, pre_y


action, E, W, S, N = map(int, input().split())

visit = [[False] * 29 for _ in range(29)]
x, y = 14, 14
visit[y][x] = True

options = [0, 1, 2, 3]

possibility = 100
result = 0

move(0)

print(result/100)
