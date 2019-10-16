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

        my = input_y
        while my < N:
            if arr[my][x] != 0 and arr[my][x] != island_num:
                # print(x, input_y)
                if arr[my][x] not in G[island_num]:
                    G[island_num].append(arr[my][x])
                    G[arr[my][x]].append(island_num)
                break
            my += 1

        while 0 <= my:
            if arr[my][x] != 0 and arr[my][x] != island_num:
                if arr[my][x] not in G[island_num]:
                    G[island_num].append(arr[my][x])
                    G[arr[my][x]].append(island_num)
                break
            my -= 1

        x += 1

    while y < N:
        if arr[y][input_x] != island_num:
            break

        mx = input_x
        while mx < M:
            if arr[y][mx] != 0 and arr[y][mx] != island_num:
                if arr[y][mx] not in G[island_num]:
                    G[island_num].append(arr[y][mx])
                    G[arr[y][mx]].append(island_num)
                break
            mx += 1
            
        while 0 <= mx:
            if arr[y][mx] != 0 and arr[y][mx] != island_num:
                if arr[y][mx] not in G[island_num]:
                    G[island_num].append(arr[y][mx])
                    G[arr[y][mx]].append(island_num)
                break
            mx -= 1
        
        y += 1


T = int(input())
for t in range(1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # pprint(arr)

    islands = []
    island_num = 1
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1:
                island_num += 1
                island_numbering(x, y)
                islands.append((x, y, island_num))

    G = [[] for _ in range(island_num+1)]
    # print(G)
    pprint(arr)
    # print(islands)

    connect_island(6, 0, 2)
    print(G)