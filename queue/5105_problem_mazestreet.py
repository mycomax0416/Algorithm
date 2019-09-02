import sys
sys.stdin = open('5105_sample_input.txt', 'r')
    # 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(x, y):
    stack.append((x, y))
    # stack += [(x, y)]
    visit[y][x] = True

    while stack:
        x, y = stack[-1][0], stack[-1][1]
        pre_x, pre_y = x, y

        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            if 0 <= nx < N and 0 <= ny < N and visit[ny][nx] == False:
                if maze[ny][nx] == 0:
                    stack.append((nx, ny))
                    # stack += [(nx, ny)]
                    visit[ny][nx] = True
                    x, y = nx, ny
                    break

                elif maze[ny][nx] == 3:
                    visit[ny][nx] = True
                    return len(stack)-1

        if pre_x == x and pre_y == y:
            x, y = stack.pop()

    return 0
       
def find():
    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                return DFS(x, y)

T = int(input())
for t in range(T):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    visit = [[False] * N for _ in range(N)]
    stack = []
    
    print('#{} {}'.format(t+1, find()))
