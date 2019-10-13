import sys
sys.stdin = open('16234_BOJ_input.txt', 'r')


# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def function(input_x, input_y):
    Queue = []
    visit[input_y][input_x] = True
    group = []

    while Queue:
        test = Queue.pop(0)
        x, y = test[0], test[1]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and visit[ny][nx] == False and L <= abs(arr[y][x]-arr[ny][nx]) <= R:
                Queue.append((nx, ny))
                group.append((nx, ny))
                visit[ny][nx] = True

    average = sum(group) // len(group)



T = int(input())
for t in range(1):
    N, L, R = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(N, L, R)
    print(arr)

    visit = [[False]*N for _ in range(N)]
    print(visit)

    # for y in range(N):
    #     for x in range(N):
    #         if visit[y][x] == False:
    #             funciont(x, y)