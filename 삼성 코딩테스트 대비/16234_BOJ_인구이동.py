import sys
from collections import deque
sys.stdin = open('16234_BOJ_input.txt', 'r')


def find():
    for y in range(N):
        for x in range(N):
            if visit[y][x] == False:
                return x, y


# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def function(input_x, input_y):
    Queue = deque()
    Queue.append((input_x, input_y))
    visit[input_y][input_x] = True
    group = [(input_x, input_y)]
    sum_group = arr[input_y][input_x]

    while Queue:
        x, y = Queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and visit[ny][nx] == False and L <= abs(arr[y][x]-arr[ny][nx]) <= R:
                Queue.append((nx, ny))
                group.append((nx, ny))
                sum_group += arr[ny][nx]
                visit[ny][nx] = True
    
    for x, y in group:
        arr[y][x] = sum_group // len(group)


T = int(input())
for t in range(T):
    N, L, R = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    move = 0
    count = 0

    while count != N*N:
        visit = [[False]*N for _ in range(N)]
        count = 0

        while visit != [[True]*N for _ in range(N)]:
            count += 1
            x, y = find()
            function(x, y)

        if count != N*N:
            move += 1

    print(move)