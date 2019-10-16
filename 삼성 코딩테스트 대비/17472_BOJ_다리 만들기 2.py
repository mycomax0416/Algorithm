import sys
sys.stdin = open('17472_BOJ_input.txt', 'r')
from collections import deque
from pprint import pprint


# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def island_numbering(input_x, input_y):
    queue = deque()
    queue.append((input_x, input_y))
    arr[input_y][input_x] = island_num
    visit = [[False]*M for _ in range(N)]

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < M and 0 <= ny < N and arr[ny][nx] == 1 and visit[ny][nx] == False:
                queue.append((nx, ny))
                arr[ny][nx] = island_num
                visit[ny][nx] = True

    
def connect_island(input_x, input_y, island_num):
    x, y = input_x, input_y

    while x < M:
        if arr[input_y][x] != island_num:
            break

        my_1, my_2 = input_y, input_y
        while my_1 < N:
            if arr[my_1][x] != 0 and arr[my_1][x] != island_num:
                if arr[my_1][x] not in G[island_num]:
                    G[island_num].append(arr[my_1][x])
                    G[arr[my_1][x]].append(island_num)
                break
            my_1 += 1

        while 0 <= my_2:
            if arr[my_2][x] != 0 and arr[my_2][x] != island_num:
                if arr[my_2][x] not in G[island_num]:
                    G[island_num].append(arr[my_2][x])
                    G[arr[my_2][x]].append(island_num)
                break
            my_2 -= 1

        x += 1

    while y < N:
        if arr[y][input_x] != island_num:
            break
        
        mx_1, mx_2 = input_x, input_x
        while mx_1 < M:
            if arr[y][mx_1] != 0 and arr[y][mx_1] != island_num:
                if arr[y][mx_1] not in G[island_num]:
                    G[island_num].append(arr[y][mx_1])
                    G[arr[y][mx_1]].append(island_num)
                break
            mx_1 += 1
            
        while 0 <= mx_2:
            if arr[y][mx_2] != 0 and arr[y][mx_2] != island_num:
                if arr[y][mx_2] not in G[island_num]:
                    G[island_num].append(arr[y][mx_2])
                    G[arr[y][mx_2]].append(island_num)
                break
            mx_2 -= 1
        
        y += 1


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    islands = []
    island_num = 1
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1:
                island_num += 1
                island_numbering(x, y)
                islands.append((x, y, island_num))

    G = [[] for _ in range(island_num+1)]
    pprint(arr)

    for island in islands:
        x, y, num = island
        connect_island(x, y, num)

    print(G)